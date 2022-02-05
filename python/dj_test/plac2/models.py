from django.db import models

cate=[("本社","本社"),("物流","物流")]
class Test(models.Model):
    hinban=models.CharField(max_length=10,verbose_name="品番")
    zaiko=models.IntegerField(verbose_name="在庫")
    category=models.CharField(max_length=10,choices=cate,verbose_name="カテゴリ")
    memo=models.TextField(blank=True)
    toroku=models.DateTimeField(auto_now_add=True,verbose_name="登録日")
    koshin=models.DateTimeField(auto_now=True,verbose_name="更新日")

    def __str__(self):
        return self.hinban

