from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    follow_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_from')
    follow_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_to')
    created_at = models.DateTimeField(auto_now_add=True)
