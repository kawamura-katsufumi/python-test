from django.shortcuts import render

def index(request):
    return render(request,"plac8/index.html")

def top(request):
    return render(request,"plac8/top.html")

def left(request):
    return render(request,"plac8/left.html")

def right(request):
    return render(request,"plac8/right.html")
