from django.forms import ModelForm
from .models import Send

class Sendform(ModelForm):
    class Meta:
        model=Send
        fields=["busho","name","send_name","send_tel"]