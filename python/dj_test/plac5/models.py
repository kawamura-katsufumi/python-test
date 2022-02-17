from django.db import models

co=[("ホワイト","ホワイト"),("ブラック","ブラック"),("レッド","レッド")]
si=[("S","S"),("M","M"),("L","L")]
class Session(models.Model):
    hinban=models.CharField("品番",max_length=10)
    hinmei=models.CharField("品名",max_length=50)
    color=models.CharField("カラー",max_length=10,choices=co)
    size=models.CharField("サイズ",max_length=5,choices=si)

    def __str__(self):
        return self.hinban


