from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json


from django.contrib import messages

from .models import User, Post, Follow, Like


@login_required
def create_post(request):
    post_text = request.POST.get("text")
    if not post_text:
        messages.error(request, "The post text cannot be empty")

    Post.objects.create(author=request.user, text=post_text)

    messages.info(request, "Successfully created a post")

    return redirect(reverse("index"))

def following_page(request, username, follow_type):
    users = None
    user = User.objects.get(username=username)

    if follow_type == "following":
        users = Follow.objects.filter(follow_from=user.id)
    else:
        users = Follow.objects.filter(follow_to=user.id)

    return render(request, "network/following.html", {
        "users": users,
        "page_type": follow_type
    })


@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    has_already_liked = Like.objects.filter(post=post, liked_by=request.user).exists()

    if has_already_liked:
        Like.objects.filter(post=post, liked_by=request.user).delete()
    else:
        Like.objects.create(post=post, liked_by=request.user)

    return redirect(request.META.get('HTTP_REFERER', reverse('index')))

@login_required
def follow(request):
    if request.method == "POST":
        uid = request.POST.get("user_id")
        user_to_follow = get_object_or_404(User, id=uid)
        already_followed = Follow.objects.filter(follow_from=request.user, follow_to=user_to_follow).exists()

        if already_followed:
            Follow.objects.filter(follow_from=request.user, follow_to=user_to_follow).delete()
            messages.success(request, f"You have unfollowed {user_to_follow.username}.")
        else:
            Follow.objects.create(follow_from=request.user, follow_to=user_to_follow)
            messages.success(request, f"You are now following {user_to_follow.username}.")

        return redirect(request.META.get('HTTP_REFERER', reverse('index')))
    else:
        messages.error(request, "Invalid request method.")
        return HttpResponseRedirect("/", status=405)

@csrf_exempt
def edit_post(request):
    if request.method != "PUT":
        return HttpResponse("Method Not Allowed", status=405)

    json_data = json.loads(request.body.decode('utf-8'))
   
    post_id = json_data.get("postId")
    text = json_data.get("text")

    found_post = get_object_or_404(Post, id=int(post_id))
    
    found_post.text = text
    found_post.save()

    return HttpResponse("Updated successfully!", status=200)

def profile_page(request, username):
    current_user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=current_user).order_by("-created_at")
    following_count = followers_count = 0

    if request.user.is_authenticated:
        following_count = Follow.objects.filter(follow_from=request.user).count()
        followers_count = Follow.objects.filter(follow_to=request.user).count()
        following = Follow.objects.filter(follow_from=request.user, follow_to=current_user).exists()

    return render(request, "network/profile.html", {
        "current_user": current_user,
        "following": following,
        "following_count": following_count,
        "followers_count": followers_count,
        "posts": user_posts,
    })    

def index(request):
    all_posts = Post.objects.all().order_by("-created_at")
    
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
