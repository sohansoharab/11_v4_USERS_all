from django import forms
from basic_app.models import UserProfileInfo, Post
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo

        fields = ('fb_profile_link', 'profile_pic')


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'content', 'thumbnail')









