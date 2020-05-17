from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from basic_app.forms import UserForm, UserProfileInfoForm, PostForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from basic_app.models import Post
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    all_posts = Post.objects.all().order_by('-id')
    return render(request, 'basic_app/index.html', {'all_posts': all_posts})


@login_required()
def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully Logged out')
    return HttpResponseRedirect(reverse('index'))


def user_register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully registered yourself')
            registered = True
            return HttpResponseRedirect(reverse('user_login'), {'messages': messages})

        elif user_form.cleaned_data['password'] != user_form.cleaned_data['confirm_password']:
            user_form.add_error('confirm_password', 'The passwords do not match')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'basic_app/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
        'messages': messages
    })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                messages.add_message(request, messages.SUCCESS, f'Hello {user.username}! You have successfully logged in')
                return redirect(reverse('index'), {'messages': messages})
            else:
                msg = 'User is not active'
                return redirect(reverse('user_login'), {'msg': msg})
        else:
            msg = 'Log in credentials are wrong'
            print('An intruder tried to login')
            print(f'USERNAME: {username}')
            print(f'PASSWORD: {password}')
            return redirect(reverse('user_login'), {'msg': msg})

    msg = 'Hello there'
    return render(request, 'basic_app/login.html', {'msg': msg})


def new_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            # post_form.author = request.USER
            post.author = request.user
            if 'thumbnail' in request.FILES:
                post.thumbnail = request.FILES['thumbnail']
            # post_form.save(commit=True)
            post.save()
            user = post.author
            messages.add_message(request, messages.SUCCESS, f'Hey {user.username} You have added a post right now')
            return redirect(reverse('index'), {'messages': messages})
        else:
            messages.add_message(request, messages.WARNING, f'Something is wrong.')
            return HttpResponseRedirect(reverse('new_post'), {'messaged': messages})
    else:
        post_form = PostForm(request.POST)
    return render(request, 'basic_app/new_post.html', {'post_form': post_form})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'basic_app/post_details.html', {'post': post})
