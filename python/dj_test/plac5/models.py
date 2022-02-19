from django.db import models

#Session
co=[("ホワイト","ホワイト"),("ブラック","ブラック"),("レッド","レッド")]
si=[("S","S"),("M","M"),("L","L")]
class Session(models.Model):
    hinban=models.CharField("品番",max_length=10)
    hinmei=models.CharField("品名",max_length=50)
    color=models.CharField("カラー",max_length=10,choices=co)
    size=models.CharField("サイズ",max_length=5,choices=si)

    def __str__(self):
        return self.hinban

#送り先
class Send(models.Model):
    sample_number=models.IntegerField("認証番号")
    busho=models.CharField("部署",max_length=10)
    name=models.CharField("担当",max_length=10)
    send_name=models.CharField("送付先",max_length=10)
    send_tel=models.CharField("送付先電話",max_length=20)

    def __str__(self):
        return str(self.sample_number)

#送付サンプル内容
class Sample(models.Model):
    sample_number=models.IntegerField("認証番号")
    hinban=models.CharField("品番",max_length=10)
    hinmei=models.CharField("品名",max_length=55)
    color=models.CharField("カラー",max_length=10)
    size=models.CharField("サイズ",max_length=5)

    def __str__(self):
        return str(self.sample_number)
