from django.shortcuts import render
from .models import Test

def list(request):
    items=Test.objects.all()
    return render(request,"plac2/list.html",{"items":items})

def detail(request,pk):
    item=Test.objects.get(pk=pk)
    return render(request,"plac2/detail.html",{"item":item})