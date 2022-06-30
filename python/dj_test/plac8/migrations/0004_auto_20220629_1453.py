# Generated by Django 3.1.7 on 2022-06-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac8', '0003_recieve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juchu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juchu_id', models.CharField(max_length=10, verbose_name='見積ID')),
                ('juchu_no', models.CharField(max_length=10, null=True, verbose_name='見積番号')),
                ('juchu_ver', models.CharField(max_length=10, null=True, verbose_name='バージョン')),
                ('status', models.CharField(max_length=10, null=True, verbose_name='ステータス')),
                ('mitsu_day', models.CharField(max_length=10, null=True, verbose_name='見積日')),
                ('juchu_day', models.EmailField(max_length=254, null=True, verbose_name='受注日')),
                ('eigyou_sei', models.EmailField(max_length=254, null=True, verbose_name='担当_姓')),
                ('eigyou_mei', models.EmailField(max_length=254, null=True, verbose_name='担当_名')),
                ('eigyou_busho', models.CharField(max_length=20, null=True, verbose_name='営業部署')),
                ('rec_cus_id', models.CharField(max_length=10, null=True, verbose_name='顧客ID')),
                ('keiro', models.CharField(max_length=10, null=True, verbose_name='流入経路')),
                ('mitsu_money', models.IntegerField(null=True, verbose_name='見積金額')),
            ],
        ),
        migrations.DeleteModel(
            name='Recieve',
        ),
    ]