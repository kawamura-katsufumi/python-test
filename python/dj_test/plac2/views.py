from cgi import test
from django.shortcuts import render,redirect
from .models import Test
from .forms import Testform

def list(request):
    items=Test.objects.all()
    return render(request,"plac2/list.html",{"items":items})

def detail(request,pk):
    item=Test.objects.get(pk=pk)
    return render(request,"plac2/detail.html",{"item":item})

def create(request):
    form=Testform()
    if request.method == "POST":
        form=Testform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request,"plac2/create.html",{"form":form})

def delete(request,pk):
    Test.objects.get(pk=pk).delete()
    return redirect("list")