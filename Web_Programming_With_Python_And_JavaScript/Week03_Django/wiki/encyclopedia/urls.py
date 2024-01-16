from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>/edit", views.edit_entry),
    path("random", views.random_entry),
    path("wiki/<str:entry_name>/", views.entry),
    path("new_entry/", views.new_entry),
]
