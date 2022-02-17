from django.shortcuts import render
from .models import Session

def index(request):
    items=Session.objects.all()
    return render(request,"plac5/index.html",{"items":items})
