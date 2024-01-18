from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import User, Auction, Bid, Comment

@login_required
def close_auction(request):
    if request.method == "POST":
        listing_id = request.POST.get("listing_id")
        listing = Auction.objects.get(id=listing_id)

        if request.user.id != listing.user.id:
            pass

        listing.status = "Closed"
        listing.save()

        return redirect(f"/listing/{listing_id}")
    else:
      return redirect("/")
    

@login_required
def place_bid(request):
    if request.method == "POST":
        bid_amount = request.POST.get("bid_amount")
        listing_id = request.POST.get("listing_id")

        listing = Auction.objects.get(id=listing_id)

        if not bid_amount or not listing_id:
            messages.error(request, "Invalid data sent")
        else:
            if int(bid_amount) <= int(listing.starting_bid):
                messages.error(request, f"Can't make a bid lower than ${listing.starting_bid}")
            else:
                Bid.objects.create(bid_amount=bid_amount, user=request.user, auction=listing)
                messages.info(request, "Successfully placed a bid")

        return redirect(f"/listing/{listing.id}")
    else:
      return redirect('index') 

def view_listing(request, id):
    found_listing = Auction.objects.get(id=id)
    found_bids = Bid.objects.filter(auction=found_listing).order_by("-bid_amount")
    found_comments = Comment.objects.filter(auction=found_listing)
    total_bids = len(found_bids)
    return render(request, "auctions/view_listing.html", {
        "listing": found_listing,
        "bids": found_bids,
        "total_bids": total_bids,
        "comments": found_comments
    })


def watchlist(request):
    return HttpResponse("This yo watchlist")

def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html")
    elif request.method == "POST":
        desc = request.POST.get("description")
        title = request.POST.get("title")
        cover_url = request.POST.get("cover_url")
        starting_bid = request.POST.get("starting_bid")

        Auction.objects.create(user_id=request.user.id, description=desc, title=title, image_url=cover_url, starting_bid=starting_bid)

        return redirect("index")


@login_required
def add_comment(request):
    user = request.user
    listing_id = request.POST.get("listing_id")
    auction = Auction.objects.get(id=listing_id)
    comment = request.POST.get("content")

    Comment.objects.create(user=user, text=comment, auction=auction)


    return redirect(request.META.get('HTTP_REFERER', None))
    

def index(request):
    active_listings = Auction.objects.filter(status="Open")
    closed_listings = Auction.objects.filter(status="Closed")

    active_listing_count = len(active_listings)
    closed_listing_count = len(closed_listings)

    return render(request, "auctions/index.html", {
        "active_listings": active_listings,
        "closed_listings": closed_listings,
        "active_listing_count": active_listing_count,
        "closed_listing_count": closed_listing_count,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
