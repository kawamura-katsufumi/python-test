# Generated by Django 3.1.7 on 2022-02-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac5', '0003_auto_20220219_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_number', models.IntegerField(verbose_name='認証番号')),
                ('hinban', models.CharField(max_length=10, verbose_name='品番')),
                ('hinmei', models.CharField(max_length=55, verbose_name='品名')),
                ('color', models.CharField(choices=[('ホワイト', 'ホワイト'), ('ブラック', 'ブラック'), ('レッド', 'レッド')], max_length=10, verbose_name='カラー')),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=5, verbose_name='サイズ')),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='sample_number',
        ),
    ]
