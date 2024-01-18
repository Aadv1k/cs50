from django.contrib import admin

from .models import Auction, Bid, Comment


admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Comment)
