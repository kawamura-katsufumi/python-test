from django.shortcuts import render

def index(request):
    return render(request,"plac4/index.html")
