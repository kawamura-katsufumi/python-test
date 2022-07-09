from django import forms
from .models import Customer

class Right_form(forms.ModelForm):
    tantou=forms.ChoiceField(
        choices=[("",""),("井上","井上"),("古川","古川"),("眞下","眞下"),("夏八木","夏八木")],
        label="担当者",
        widget=forms.Select(attrs={"class":"form-select"})
    )
    check_dm=forms.BooleanField(label="DM", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    check_tel=forms.BooleanField(label="TEL", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)
    check_gaisho=forms.BooleanField(label="外商", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),required=False)

    bikou=forms.CharField(label="備考",widget=forms.Textarea(attrs={"class":"form-control","rows":"3"}))

    class Meta:
        model=Customer
        fields=["tantou","check_dm","check_tel","check_gaisho","bikou"]


