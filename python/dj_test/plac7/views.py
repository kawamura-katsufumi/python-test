from django.shortcuts import render
from django.http import JsonResponse
from plac6.models import Master
from .forms import Plac7form

def index(request):
    form=Plac7form()
    return render(request,"plac7/index.html",{"form":form})


def ajax_number(request):
    number1 = int(request.POST.get('number1'))
    number2 = int(request.POST.get('number2'))
    hinban = request.POST.get('hinban')
    plus = number1 + number2
    minus = number1 - number2
    items= Master.objects.filter(hinban__contains = hinban).distinct().values_list("color_name",flat=True)
    items=list(items)
    # print(items)
    d = {
        'plus': plus,
        'minus': minus,
        'hinban':hinban,
        'items':items,
    }
    # print(d)
    return JsonResponse(d)

def selenium_test(request):
    pass