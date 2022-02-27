from curses import meta
from tkinter import CASCADE
from urllib import request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    followers = models.ManyToManyField('User', null=True ,related_name="followed")


    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    creator = models.ForeignKey(User , on_delete=CASCADE, related_name="creatorPosts")
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, blank=True, null=True)
    likeNum = models.PositiveIntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "creator": self.created,
            "body": self.body,
            "created": self.created.strftime("%b %d %Y, %I:%M %p"),
            "updated": self.updated.strftime("%b %d %Y, %I:%M %p"),
            "liked": self.liked,
            "likeNum": self.likeNum
        }

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f"{self.creator} Wrote {self.body} on {self.created.strftime('%d/%m/%Y, %H:%M%p')} with {self.liked.count()} likes"
