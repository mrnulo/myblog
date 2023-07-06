from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=110, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title: CharField = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
