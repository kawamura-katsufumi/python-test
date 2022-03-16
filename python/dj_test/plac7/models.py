from django.db import models

kata=[("1","01"),("2","02"),("3","03")]
class Plac7(models.Model):
    jan=models.CharField(max_length=20)
    hinban=models.CharField(max_length=10)
    kataban=models.CharField(max_length=5,choices=kata)
