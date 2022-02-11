from django.shortcuts import render,redirect
from .models import Omote,Ura
from django.core.paginator import Paginator
from .forms import Omoteform,Uraform

def omote(request,num=1):
    items=Omote.objects.all()
    pages=Paginator(items, 4)
    data=pages.get_page(num)

    ###　実験　###
    dic={}
    jdata1=Ura.objects.all()
    jdata2=Ura.objects.distinct().values_list("club",flat=True)
    for item in jdata2:
        a=[]
        for i in jdata1:
            if str(item) == str(i):
                b=str(i.name2)
                a.append(b)
        a=" , ".join(a)
        dic[item]=a
    ###　ここまで　###

    params={
        "data":data,
        "data2":dic,
        "form1":Omoteform(),
        "form2":Uraform(),
            }
   
    return render(request,"plac3/omote.html",params)

def name(request):
    form=Omoteform(request.POST)
    if form.is_valid():
        form.save()
        return redirect("omote")

def club(request):
    form=Uraform(request.POST)
    if form.is_valid():
        form.save()
        return redirect("omote")

def omote_test(request):
    test1=request.POST["test_name"]
    test2=request.POST["test_age"]
    Omote.objects.create(name=test1,age=test2)
    return redirect("omote")

def delete(request,pk):
    Omote.objects.get(pk=pk).delete()
    return redirect("omote")