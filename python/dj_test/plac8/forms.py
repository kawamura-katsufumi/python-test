from django import forms

class Right_form(forms.Form):
    tantou=forms.ChoiceField(
        choices=[("",""),("井上","井上"),("古川","古川"),("眞下","眞下"),("夏八木","夏八木")],
        label="担当者",
        widget=forms.Select(attrs={"class":"form-control"})
    )
    # status_dm=forms.BooleanField(label="DM",required=False,attrs={"class":"form-control"})
    # status_tel=forms.BooleanField(label="TEL",required=False,attrs={"class":"form-control"})
    # status_gaisho=forms.BooleanField(label="外商",required=False,attrs={"class":"form-control"})

    cus_id=forms.CharField(label="顧客ID",widget=forms.TextInput(attrs={"class":"form-control"}))
    com=forms.CharField(label="会社",widget=forms.TextInput(attrs={"class":"form-control"}))
    busho=forms.CharField(label="部課名",widget=forms.TextInput(attrs={"class":"form-control"}))
    sei=forms.CharField(label="姓",widget=forms.TextInput(attrs={"class":"form-control"}))
    mei=forms.CharField(label="名",widget=forms.TextInput(attrs={"class":"form-control"}))
    sei_kana=forms.CharField(label="せい",widget=forms.TextInput(attrs={"class":"form-control"}))
    mei_kana=forms.CharField(label="めい",widget=forms.TextInput(attrs={"class":"form-control"}))
    yubin=forms.CharField(label="郵便番号",widget=forms.TextInput(attrs={"class":"form-control"}))
    pref=forms.CharField(label="都道府県",widget=forms.TextInput(attrs={"class":"form-control"}))
    city=forms.CharField(label="市区町村",widget=forms.TextInput(attrs={"class":"form-control"}))
    banchi=forms.CharField(label="番地",widget=forms.TextInput(attrs={"class":"form-control"}))
    build=forms.CharField(label="建物名",widget=forms.TextInput(attrs={"class":"form-control"}))
    tel=forms.CharField(label="電話番号",widget=forms.TextInput(attrs={"class":"form-control"}))
    mob=forms.CharField(label="携帯番号",widget=forms.TextInput(attrs={"class":"form-control"}))
    fax=forms.CharField(label="FAX番号",widget=forms.TextInput(attrs={"class":"form-control"}))
    mail1=forms.EmailField(label="メール1",widget=forms.TextInput(attrs={"class":"form-control"}))
    mail2=forms.EmailField(label="メール2",widget=forms.TextInput(attrs={"class":"form-control"}))
    mail3=forms.EmailField(label="メール3",widget=forms.TextInput(attrs={"class":"form-control"}))
    bikou=forms.CharField(label="備考",widget=forms.TextInput(attrs={"class":"form-control","rows":"3"}))


