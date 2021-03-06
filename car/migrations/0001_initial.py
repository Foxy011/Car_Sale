# Generated by Django 2.1.15 on 2021-12-07 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.SmallIntegerField(verbose_name='Цена')),
                ('year', models.SmallIntegerField(verbose_name='Год выпуска')),
                ('name', models.CharField(max_length=255, verbose_name='Имя владельца')),
                ('car_cat', models.CharField(default='do 1990', max_length=255, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='CarMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_mark', models.CharField(max_length=255, verbose_name='Марка авто')),
            ],
            options={
                'verbose_name': 'Марка авто',
                'verbose_name_plural': 'Марка авто',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=255, verbose_name='Модель авто')),
            ],
            options={
                'verbose_name': 'Модель авто',
                'verbose_name_plural': 'Модель авто',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('min_date', models.SmallIntegerField(verbose_name='min_date')),
                ('max_date', models.SmallIntegerField(verbose_name='max_date')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='car_mdl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_models', to='car.CarModel', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_mrk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_marks', to='car.CarMark', verbose_name='Марка'),
        ),
    ]
