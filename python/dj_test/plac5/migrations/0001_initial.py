# Generated by Django 3.1.7 on 2022-02-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinban', models.CharField(max_length=10, verbose_name='品番')),
                ('hinmei', models.CharField(max_length=50, verbose_name='品名')),
                ('color', models.CharField(max_length=10, verbose_name='カラー')),
                ('size', models.CharField(max_length=5, verbose_name='サイズ')),
            ],
        ),
    ]
