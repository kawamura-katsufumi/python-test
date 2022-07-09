# Generated by Django 3.1.7 on 2022-07-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac8', '0012_auto_20220708_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='check_dm',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='check_gaisho',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='check_tel',
        ),
        migrations.AddField(
            model_name='customer',
            name='dm_day',
            field=models.DateField(blank=True, null=True, verbose_name='DM'),
        ),
        migrations.AddField(
            model_name='customer',
            name='gaisho_day',
            field=models.DateField(blank=True, null=True, verbose_name='外商'),
        ),
        migrations.AddField(
            model_name='customer',
            name='tel_day',
            field=models.DateField(blank=True, null=True, verbose_name='TEL'),
        ),
    ]