from django.shortcuts import render,redirect
from .models import Session,Shozoku,Send,Sample
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import Sendform
from django.db.models import Max

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

def kakutei(request):
    num=Send.objects.all().aggregate(Max("sample_number"))
    x=num["sample_number__max"]
    #届け先 
    Send.objects.create(
        sample_number=x+1,
        busho=Shozoku.objects.get(name=request.user).busho,
        name=request.user,
        send_name=request.POST["send_name"],
        send_tel=request.POST["send_tel"]
        )

    # #サンプル内容
    all_id=request.session.get("sample",{})
    for key,value in all_id.items():
        data=Session.objects.get(id=key)
        Sample.objects.create(
            sample_number=x+1,
            hinban=data.hinban,
            hinmei=data.hinmei,
            color=data.color,
            size=data.size
        )
    del request.session["sample"]
    return redirect("index")


def rireki(request):
    if request.user.is_superuser:
        items=Send.objects.all()
        for sam in items:
            samples=Sample.objects.filter(sample_number=sam.sample_number)
        return render(request,"plac5/rireki.html",{"items":items,"samples":samples})