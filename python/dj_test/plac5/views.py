from django.shortcuts import render,redirect
from .models import Session,Shozoku
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import Sendform

def index(request):
    items=Session.objects.all()
    return render(request,"plac5/index.html",{"items":items})


def add(request,pk):

    # request.session.modified = True

    item=Session.objects.get(pk=pk)

    if "sample" in request.session:

        if str(item.id) in request.session["sample"]:
            messages.warning(request,"既に追加されています！")
            return redirect("index")
        else:
            request.session["sample"][str(item.id)]=1
            messages.success(request,"サンプルを追加しました！")
            return redirect("index")
                
        # print(request.session["sample"])

    else:
        request.session["sample"]={str(item.id):1}

        # print(request.session["sample"])
    
        messages.success(request,"サンプルを追加しました！")

    return redirect("index")


def delete(request):
    del request.session["sample"]
    # print("削除OK")
    return redirect("index")


def send(request):
    form=Sendform()
    shozoku=Shozoku.objects.get(name=request.user)
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
    return render(request,"plac5/send.html",{"context":context,"form":form,"shozoku":shozoku})

def send_delete(request,pk):
    del request.session["sample"][str(pk)]
    return redirect("send")