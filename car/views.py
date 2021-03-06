from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


from car.models import *
from car.forms import CarAddForm

# Create your views here.

def cars_list(request):

    car_list = Car.objects.all()

    context = {
        'car_list': car_list,
    }

    return render(request, 'car_list.html', context)


def car_form(request):
    if request.method == 'POST':
        form = CarAddForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            year = form.cleaned_data['year']
            price = form.cleaned_data['price']
            name = form.cleaned_data['name']
            car_mrk = form.cleaned_data['car_mrk']
            car_mdl = form.cleaned_data['car_mdl']


            qwe = Car(
                year = year,price=price,name=name,number=number,car_mrk=car_mrk,car_mdl=car_mdl
            )
            qwe.save()
            return render(request, 'thank_you.html')

    else:
        form = CarAddForm()
    return render(request, 'car_form_add.html', {'form': form})


def rest(request):
    my_model = Car.objects.all()
    response = serializers.serialize("json", my_model)
    return HttpResponse(response, content_type='application/json')