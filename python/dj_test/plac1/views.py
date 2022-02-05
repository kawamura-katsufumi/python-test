from django.shortcuts import render

def moto(request):
    return render(request,"plac1/moto.html")

def index(request):
    username="川村"
    return render(request,"plac1/index.html",{"username":username})

def about(request):
    return render(request,"plac1/about.html")