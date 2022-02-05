from django.shortcuts import render
from .models import Omote

def omote(request):
    items=Omote.objects.all()
    return render(request,"plac3/omote.html",{"items":items})
