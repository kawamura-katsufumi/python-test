from django.shortcuts import render,redirect
import io
import csv
from django.http import HttpResponse

def index(request):
    return render(request,"plac6/index.html")


def csv_import(request):
    if 'csv' in request.FILES:
        data = io.TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        print(data)
        csv_content = csv.reader(data)
        print(csv_content)
        for i in csv_content:
            hiragana, created = Hiragana.objects.get_or_create(moji = i[1])
            hiragana.pk = i[0]
            hiragana.moji = i[1]
            hiragana.save()
        return redirect('index')
    else:
        return redirect('index')


# xxx.objects.update_or_create(
#  # ユニークな値
#   name=name,

#  # 更新もしくは新規で追加したい値
#   defalults={
#   "name": name, "age": age  
#  }
# )
