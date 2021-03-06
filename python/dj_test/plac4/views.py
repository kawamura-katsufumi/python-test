from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Photo,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from django.contrib import messages
from django.views.decorators.http import require_POST


def index(request):
    photos=Photo.objects.all().order_by("-created_at")
    return render(request,"plac4/index.html",{"photos":photos})

def users_detail(request,pk):
    user=User.objects.get(pk=pk)
    photos=user.photo_set.all().order_by("-created_at")
    return render(request,"plac4/users_detail.html",{"user":user,"photos":photos})

def signup(request):
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_username=request.POST["username"]
            input_password=request.POST["password1"]
            new_user=authenticate(username=input_username,password=input_password)
            if new_user is not None:
                login(request,new_user)
                return redirect("users_detail",pk=new_user.pk)
    else:
        form=UserCreationForm()
    return render(request,"plac4/signup.html",{"form":form})

@login_required
def photos_new(request):
    if request.method == "POST":
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.user=request.user
            photo.save()
            messages.success(request,"投稿が完了しました！")
        return redirect("users_detail",pk=request.user.pk)
    else:
        form=PhotoForm()
    return render(request,"plac4/photos_new.html",{"form":form})

def photos_detail(request,pk):
    photo=Photo.objects.get(pk=pk)
    return render(request,"plac4/photos_detail.html",{"photo":photo})

@require_POST
def photos_delete(request,pk):
    Photo.objects.get(pk=pk,user=request.user).delete()
    return redirect("users_detail",pk=request.user.pk)

def photos_category(request,category):
    category=Category.objects.get(title=category)
    photos=Photo.objects.filter(category=category).order_by("-created_at")
    return render(request,"plac4/index.html",{"category":category,"photos":photos})