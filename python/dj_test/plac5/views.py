from django.shortcuts import render,redirect
from .models import Session

def index(request):
    items=Session.objects.all()
    return render(request,"plac5/index.html",{"items":items})

def add(request,pk):

    # del request.session['sample']

    item=Session.objects.get(pk=pk)

    if "sample" in request.session:
        
        print(request.session["sample"])

        # print("あり")
        if item.hinban not in request.session["sample"]:

            # print(request.session["sample"])
            request.session["sample"][item.hinban]=1
        
        
        print(request.session["sample"])



    else:
        print("なし")
        request.session["sample"]={item.hinban:1}
        
    return redirect("index")



def get_context_data(self, **kwargs):
        # セッションを追加する
        self.request.session['add_session'] = 'セッション追加'
        self.request.session['array_session'] = dict(a='配列も', b='セッションに保管できます')
        
        return redirect("index")