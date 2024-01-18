from django.contrib import admin

from .models import Auction, Bid, Comment, User


admin.site.register(Auction)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment)
