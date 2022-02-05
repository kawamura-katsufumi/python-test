from django.shortcuts import render
from .models import Omote,Ura

def omote(request):
    params={
        "items":Omote.objects.all(),
        "clubs":Ura.objects.all(),
            }
   
    return render(request,"plac3/omote.html",params)
