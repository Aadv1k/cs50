from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import User, Post


@login_required
def create_post(request):
    post_text = request.POST.get("text")
    if not post_text:
        messages.error(request, "The post text cannot be empty")

    Post.objects.create(author=request.user, text=post_text)

    messages.info(request, "Successfully created a post")

    return redirect(reverse("index"))

def profile_page(request, username):
    current_user = User.objects.get(username=username)
    user_posts = Post.objects.filter(author_id=current_user).order_by("-created_at")

    return render(request, "network/profile.html", {
        "current_user": current_user,
        "posts": user_posts,
    })
    

def index(request):
    all_posts = Post.objects.all()
    return render(request, "network/index.html", {
        "posts": all_posts
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
