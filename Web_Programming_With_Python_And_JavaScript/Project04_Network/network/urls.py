
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("create_post", views.create_post, name="create_post"),
    path("profile/<str:username>", views.profile_page, name="profile_page"),
    path("profile/<str:username>/following", views.following_page, {'follow_type': 'following'}, name="following"),
    path("profile/<str:username>/followers", views.following_page, {'follow_type': 'followers'}, name="followers"),

    path("follow", views.follow, name="follow"),
    path("like/<str:post_id>", views.like, name="like")

]
