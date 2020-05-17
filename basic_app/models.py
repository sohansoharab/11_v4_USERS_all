from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from datetime import datetime

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields
    fb_profile_link = models.URLField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=datetime.now)
    thumbnail = models.ImageField(upload_to='post_thumb', blank=True)
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title