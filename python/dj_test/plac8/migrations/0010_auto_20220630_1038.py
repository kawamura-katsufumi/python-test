# Generated by Django 3.1.7 on 2022-06-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac8', '0009_auto_20220630_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100, null=True, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_rec_id',
            field=models.CharField(max_length=10, null=True, verbose_name='見積ID'),
        ),
        migrations.AlterField(
            model_name='recieve',
            name='rec_cus_id',
            field=models.CharField(max_length=10, null=True, verbose_name='顧客ID'),
        ),
    ]