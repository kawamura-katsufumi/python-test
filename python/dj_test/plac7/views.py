from django.shortcuts import render,redirect
from django.http import JsonResponse
from plac6.models import Master
from .forms import Plac7form
import urllib.request
from selenium import webdriver
# import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests

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

options = Options()

def selenium_test(request):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.yahoo.co.jp/")
    return render(request,"plac7/index.html")