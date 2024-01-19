from django.contrib import admin

from .models import User, Post, Like, Follow

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Follow)

