from tkinter import CASCADE
from django.db import models

class Omote(models.Model):
    name=models.CharField(max_length=10,verbose_name="名前")
    age=models.IntegerField(verbose_name="年齢")

    def __str__(self):
        return self.name

class Ura(models.Model):
    name2=models.ForeignKey(Omote,verbose_name="名前",on_delete=models.CASCADE)
    club=models.CharField(max_length=20,verbose_name="クラブ")

    def __str__(self):
        return self.club
