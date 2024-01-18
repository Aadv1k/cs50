from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Bid

def place_bid(request):
    if request.method == "POST":
        bid_amount = request.POST.get("bid_amount")
        listing_id = request.POST.get("listing_id")

        if not bid_amount or not listing_id:
            return HttpResponse("403: Invalid data sent", status=403)


        initial_bid = Auction.objects.get(id=listing_id)

        if bid_amount <= 

        Bid.objects.create(bid_amount="")

    else:
        return HttpResponse("405: Method not allowed ", status=405)


    

def view_listing(request, id):
    found_listing = Auction.objects.get(id=id)
    return render(request, "auctions/view_listing.html", {
        "listing": found_listing
    })


def watchlist(request):
    return HttpResponse("This yo watchlist")

def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html")

    return HttpResponse("Welcome to create listing")


def index(request):
    listings = Auction.objects.all()
    listing_count = len(listings)
    return render(request, "auctions/index.html", {
        "listing_count": listing_count,
        "listings": listings
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
