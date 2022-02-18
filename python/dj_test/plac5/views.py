from django.shortcuts import render,redirect
from .models import Session

def index(request):
    items=Session.objects.all()
    return render(request,"plac5/index.html",{"items":items})


def add(request,pk):

    # request.session.modified = True

    item=Session.objects.get(pk=pk)

    if "sample" in request.session:
        
        # print(request.session["sample"])

        # # print("あり")
        # if item.hinban not in request.session["sample"]:

        #     # print(request.session["sample"])
        request.session["sample"][item.hinban]=1
        
        
        print(request.session["sample"])



    else:
        print("なし")
        request.session["sample"]={item.hinban:1}

        print(request.session["sample"])
        
    return redirect("index")


def delete(request):
    del request.session['sample']
    print("削除OK")
    return redirect("index")