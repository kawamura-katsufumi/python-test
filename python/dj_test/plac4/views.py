from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Photo


def index(request):
    photos=Photo.objects.all().order_by("-created_at")
    return render(request,"plac4/index.html",{"photos":photos})

def users_detail(request,pk):
    user=User.objects.get(pk=pk)
    photos=user.photo_set.all().order_by("-created_at")
    return render(request,"plac4/users_detail.html",{"user":user,"photos":photos})
