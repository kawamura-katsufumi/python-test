# Generated by Django 3.1.7 on 2022-06-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac8', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='bikou',
            field=models.TextField(null=True, verbose_name='備考'),
        ),
    ]
