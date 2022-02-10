from django.forms import ModelForm
from django import forms
from .models import Omote,Ura

class Omoteform(ModelForm):
    class Meta:
        model=Omote
        fields=["name","age"]


class Uraform(ModelForm):
    class Meta:
        model=Ura
        fields=["name2","club"]

