from django.shortcuts import render
from .models import Omote,Ura
from django.core.paginator import Paginator

def omote(request,num=1):
    items=Omote.objects.all()
    pages=Paginator(items, 4)
    data=pages.get_page(num)
    params={
        "data":data,
        "clubs":Ura.objects.all(),
            }
   
    return render(request,"plac3/omote.html",params)
