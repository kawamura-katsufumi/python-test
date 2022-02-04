from django.shortcuts import render

def moto(request):
    return render(request,"plac1/moto.html")

def index(request):
    return render(request,"plac1/index.html")

def about(request):
    return render(request,"plac1/about.html")