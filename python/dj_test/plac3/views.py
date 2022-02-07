from django.shortcuts import render,redirect
from .models import Omote,Ura
from django.core.paginator import Paginator
from .forms import Omoteform,Uraform

def omote(request,num=1):
    items=Omote.objects.all()
    pages=Paginator(items, 4)
    data=pages.get_page(num)

    params={
        "data":data,
        "clubs":Ura.objects.all(),
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