from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

from .models import *
from django import forms
from django.forms import ModelForm, TextInput

class newPost(ModelForm):
    class Meta:
        model = Post
        fields = {'body'}
        widgets = {
            'body': TextInput(attrs={
                'class': "form-control",

            })
        }


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {
        "form" : newPost(),
        "posts" : posts,
        'page_obj': page_obj
    })

def profile(request, user):
    profile = User.objects.get(username = user)
    posts = Post.objects.filter(creator = profile.id)
    followersN = profile.followers.count()
    follow = User.objects.get(id = profile.id)
    followingN = User.objects.filter(followers = profile.id).count()
    if request.user in follow.followers.all():
        followed = True
    else:
        followed = False
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/profile.html", {
        "posts" : posts,
        "profileUser" : user,
        "followersN" : followersN,
        "followed" : followed,
        "followingN" : followingN,
        'page_obj': page_obj
    })

def following(request, user):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    userid = User.objects.get(username = user).id
    profile = User.objects.filter(followers = userid)
    posts = Post.objects.filter(creator__in = profile)
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print (profile)
    return render(request, "network/following.html", {
        "posts" : posts,
        'page_obj': page_obj
        })
    

def follow(request, user):
    profile = User.objects.get(username = user)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    follow = User.objects.get(id = profile.id)
    if follow == None or request.user not in follow.followers.all():
        follow.followers.add(request.user)
    else:
        follow.followers.remove(request.user)
    follow.save()
    return HttpResponseRedirect(reverse("profile", args=[user]))

@csrf_exempt
@login_required
def like(request, pk):
    post = Post.objects.get(id = pk)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == "PUT":
        if request.user in post.liked.all():
            like = False
            post.liked.remove(request.user)
        else:
            like = True
            post.liked.add(request.user)
        post.likeNum = post.liked.count()
        post.save()
        return JsonResponse({'like':like, 'likeNum': post.likeNum},status=200)

@csrf_exempt
@login_required
def edit(request, pk):
    post = Post.objects.get(id = pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        if request.user != post.creator:
                return HttpResponse(status=401)
        post.body = data["body"]
        post.save()
        return JsonResponse({},status=200)
        



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def new(request):
    if request.method == "POST":
        new = newPost(request.POST)
        if new.is_valid():
            new_Post = new.save(commit=False)
            new_Post.creator = request.user
            new_Post.save()

            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))