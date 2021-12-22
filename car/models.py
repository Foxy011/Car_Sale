from django.db import models

# Create your models here.



class CarMark(models.Model):
    car_mark = models.CharField(max_length=255, verbose_name='Марка авто')

    def __str__(self):
        return self.car_mark

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марка авто'



class CarModel(models.Model):
    car_model = models.CharField(max_length=255, verbose_name='Модель авто')

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модель авто'


class Car(models.Model):

    price = models.SmallIntegerField(verbose_name='Цена в $')
    year = models.SmallIntegerField(verbose_name='Год выпуска', default='2021')
    name = models.CharField(max_length=255, verbose_name='Имя владельца')

    number = models.CharField(verbose_name='Номер', max_length=255, default='+996')
    car_mrk = models.ForeignKey(CarMark, verbose_name='Марка', related_name='car_marks', on_delete=models.CASCADE)
    car_mdl = models.ForeignKey(CarModel, verbose_name='Модель', related_name='car_models', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'