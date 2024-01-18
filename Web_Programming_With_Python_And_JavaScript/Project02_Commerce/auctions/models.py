from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class User(AbstractUser):
    pass

class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

CATEGORIES = tuple((x, x.upper()) for x in ["Fashion", "None", "Toys", "Electronics", "Home"])
STATUS = tuple((x, x.upper()) for x in ["Closed", "Open", "Deleted"])

class Auction(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    category  = models.CharField(max_length=32, choices=CATEGORIES, default="None", null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=32, choices=STATUS, default="Open", null=True)

    def __str__(self):
        return self.title

class Bid(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(Base):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
