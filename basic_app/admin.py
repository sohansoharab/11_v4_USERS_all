from django.contrib import admin
from basic_app.models import UserProfileInfo, Post, Comment

# Register your models here.


admin.site.register(UserProfileInfo)
admin.site.register(Post)
admin.site.register(Comment)