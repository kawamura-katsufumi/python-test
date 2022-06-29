from django.db import models

class Customer(models.Model):
    cus_id=models.CharField("顧客ID",max_length=10)
    sei=models.CharField("姓",max_length=10,null=True)
    mei=models.CharField("名",max_length=10,null=True)
    sei_kana=models.CharField("姓かな",max_length=10,null=True)
    mei_kana=models.CharField("名かな",max_length=10,null=True)
    mail1=models.EmailField("メール1",null=True)
    mail2=models.EmailField("メール2",null=True)
    mail3=models.EmailField("メール3",null=True)
    yubin=models.CharField("郵便番号",max_length=10,null=True)
    pref=models.CharField("都道府県",max_length=10,null=True)
    city=models.CharField("市区町村",max_length=50,null=True)
    banchi=models.CharField("番地",max_length=50,null=True)
    build=models.CharField("建物",max_length=50,null=True)
    com=models.CharField("会社",max_length=50,null=True)
    busho=models.CharField("部署",max_length=50,null=True)
    tel=models.CharField("電話",max_length=20,null=True)
    mob=models.CharField("携帯",max_length=20,null=True)
    fax=models.CharField("FAX",max_length=20,null=True)
    toroku=models.CharField("登録日",max_length=10,null=True)
    kensu=models.IntegerField("件数",null=True)
    money=models.IntegerField("金額",null=True)
    tantou=models.CharField("担当",max_length=10,null=True)
    check_dm=models.BooleanField("DM",default=False)
    check_tel=models.BooleanField("TEL",default=False)
    check_gaisho=models.BooleanField("外商",default=False)
    bikou=models.TextField("備考",null=True)

    def __str__(self):
        return self.cus_id


class Recieve(models.Model):
    rec_id=models.CharField("見積ID",max_length=10)
    rec_no=models.CharField("見積番号",max_length=10,null=True)
    rec_ver=models.CharField("バージョン",max_length=10,null=True)
    status=models.CharField("ステータス",max_length=10,null=True)
    mitsu_day=models.CharField("見積日",max_length=10,null=True)
    rec_day=models.CharField("受注日",max_length=10,null=True)
    eigyou_sei=models.CharField("担当_姓",max_length=10,null=True)
    eigyou_mei=models.CharField("担当_名",max_length=10,null=True)
    eigyou_busho=models.CharField("営業部署",max_length=20,null=True)
    rec_cus_id=models.CharField("顧客ID",max_length=10,null=True)
    keiro=models.CharField("流入経路",max_length=10,null=True)
    mitsu_money=models.IntegerField("見積金額",null=True)

    def __str__(self):
        return self.rec_id

class Item(models.Model):
    item_rec_id=models.CharField("見積ID",max_length=10)
    item_name=models.CharField("品名",max_length=100)

    def __str__(self):
        return self.item_name
