# Generated by Django 3.1.7 on 2022-02-23 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plac5', '0008_auto_20220221_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send',
            name='sample_number',
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plac5.send'),
        ),
    ]