# Generated by Django 3.1.7 on 2022-07-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plac9', '0004_auto_20220703_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tantou',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='担当'),
        ),
    ]
