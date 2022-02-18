from django.shortcuts import render,redirect
from .models import Session
from django.contrib import messages

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
        request.session["sample"][str(item.id)]=1
        
        
        print(request.session["sample"])



    else:
        print("なし")
        request.session["sample"]={str(item.id):1}

        print(request.session["sample"])
    
    messages.success(request,"サンプルを追加しました！")
    return redirect("index")


def delete(request):
    del request.session["sample"]
    print("削除OK")
    return redirect("index")


def send(request):
    all_id=request.session.get("sample",{})
    context={}
    for key,value in all_id.items():
        data=Session.objects.get(id=key)
        context[key]={
        "hinban":data.hinban,
        "hinmei":data.hinmei,
        "color":data.color,
        "size":data.size,
        }
    return render(request,"plac5/send.html",{"context":context})

def send_delete(request,pk):
    print(pk)
    del request.session["sample"][str(pk)]
    return redirect("send")