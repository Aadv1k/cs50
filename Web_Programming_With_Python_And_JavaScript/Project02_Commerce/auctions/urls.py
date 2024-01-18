from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:id>", views.view_listing, name="listing"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("add_comment", views.add_comment, name="add_comment"),
    path("close_auction", views.close_auction, name="close_auction"),
    path("place_bid", views.place_bid, name="place_bid")
]
