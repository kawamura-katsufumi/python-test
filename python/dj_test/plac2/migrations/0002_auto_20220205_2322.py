# Generated by Django 3.1.7 on 2022-02-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='memo',
            field=models.TextField(blank=True, verbose_name='メモ'),
        ),
    ]
