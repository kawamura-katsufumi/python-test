from django.shortcuts import render

def moto(request):
    return render(request,"plac1/moto.html")

def index(request):
    username="テンテン"
    return render(request,"plac1/index.html",{"username":username})

def about(request):
    params={
        "num":1234567,
        "skills":["VBA","Python","Chinese"],
    }
    return render(request,"plac1/about.html",params)