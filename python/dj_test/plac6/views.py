from django.shortcuts import render,redirect
import io
import csv
from django.http import HttpResponse
from .models import Master


def index(request):
    return render(request,"plac6/index.html")

def master(request):
    if 'csv' in request.FILES:
        data = io.TextIOWrapper(request.FILES['csv'].file)
        csv_content = csv.reader(data)

        header =next(csv_content) #タイトルを読み飛ばす

        for i in csv_content:
            Master.objects.update_or_create(
                jan = i[7],
                defaults={
                    "brand": i[0],
                    "hinban": i[1],
                    "hinmei": i[2],
                    "color_no": i[3],
                    "color_name": i[4],
                    "size_no": i[5],
                    "size_name": i[6],
                    "jan": i[7],
                }  
            )
        return redirect('index')
    else:
        return redirect('index')


def csv_import(request):
    if 'csv2' in request.FILES:

        #------読込-------
        data = io.TextIOWrapper(request.FILES['csv2'].file)
        csv_content = csv.reader(data)
        header=next(csv_content)

        #------HTMLへ------
        dict={}
        i=0
        for line in csv_content:
            dict[i]={
                "hinmei":line[1],
                "num":line[6],
                "sku":line[8],
            }
            i+=1
            mitsumori=line[7]
        
        #------出力------
        file=request.FILES['csv2']
        if "キャブ" in str(file):
            maker="CAB"




        elif "トムス" in str(file):
            maker="TOMS"





        return render(request,"plac6/index.html",{"dict":dict,"mitsumori":mitsumori,"maker":maker})
    
    else:
        return redirect('index')


def csvexport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="somefilename.csv"'

    writer = csv.writer(response)
    for moji in Hiragana.objects.all():
        writer.writerow([moji.pk, moji.moji])
    return response