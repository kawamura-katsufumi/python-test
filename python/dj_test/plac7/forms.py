from django import forms

class Plac7form(forms.Form):
    jan=forms.CharField(label="JAN",widget=forms.TextInput(attrs={"class":"form-control","readonly":"readonly"}))
    hinban=forms.CharField(label="品番",widget=forms.TextInput(attrs={"class":"form-control"}))
    kataban=forms.ChoiceField(
        choices=[("",""),("1","01"),("2","02"),("3","03")],
        label="型番",       
        widget=forms.Select(attrs={"class":"form-control"})
        )