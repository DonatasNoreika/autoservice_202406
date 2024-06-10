from django.shortcuts import render
from .models import Service, Order, Car


# Create your views here.

def index(request):
    services = Service.objects.all().count()
    orders = Order.objects.filter(status="d").count()
    cars = Car.objects.all().count()
    context = {
        'services': services,
        'orders': orders,
        'cars': cars,
    }
    return render(request, template_name="index.html", context=context)


def cars(request):
    return render(request, template_name="cars.html", context={"cars": Car.objects.all()})


def car(request, car_id):
    car = Car.objects.get(pk=car_id)
    context = {
        'car': car,
    }
    return render(request, "car.html", context=context)
