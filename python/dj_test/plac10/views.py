from django.shortcuts import render

def index(request):
    return render(request,"plac10/index.html")
