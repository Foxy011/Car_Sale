# Generated by Django 2.1.15 on 2021-12-14 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_cat',
        ),
        migrations.AddField(
            model_name='car',
            name='number',
            field=models.CharField(default='+996', max_length=255, verbose_name='Номер'),
        ),
    ]
