from django.contrib import admin
from car.models import *

# Register your models here.


@admin.register(CarMark)
class AdminCarMark(admin.ModelAdmin):
    list_display = ('id', 'car_mark')
    list_filter = ('car_mark',)


@admin.register(CarModel)
class AdminCarModel(admin.ModelAdmin):
    list_display = ('id', 'car_model')
    list_filter = ('car_model',)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('id', 'price', 'year', 'number', 'name', 'car_mrk', 'car_mdl')
    list_filter = ('price', 'year', 'number', 'name')