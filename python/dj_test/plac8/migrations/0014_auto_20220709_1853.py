# Generated by Django 3.1.7 on 2022-07-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac8', '0013_auto_20220709_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dm_day',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='DM'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gaisho_day',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='外商'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tel_day',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='TEL'),
        ),
    ]