from pyexpat import model
from django.forms import ModelForm
from .models import Test

class Testform(ModelForm):
    class Meta:
        model=Test
        fields=["hinban","zaiko","category","memo"]