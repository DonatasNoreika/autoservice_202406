from django.shortcuts import render
from .models import Service, Order, Car
from django.views.generic import (ListView,
                                  DetailView)
from django.core.paginator import Paginator
from django.db.models import Q

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
    cars = Car.objects.all()
    paginator = Paginator(cars, per_page=9)
    page_number = request.GET.get("page")
    paged_cars = paginator.get_page(page_number)
    return render(request, template_name="cars.html", context={"cars": paged_cars})


def car(request, car_id):
    car = Car.objects.get(pk=car_id)
    context = {
        'car': car,
    }
    return render(request, "car.html", context=context)


class OrderListView(ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"
    paginate_by = 5


class OrderDetailView(DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"


def search(request):
    query = request.GET.get('query')
    cars = Car.objects.filter(Q(client_name__icontains=query) | Q(car_model__make__icontains=query) | Q(car_model__model__icontains=query) | Q(license_plate__icontains=query) | Q(vin_code__icontains=query))
    context = {
        "cars": cars,
        "query": query,
    }
    return render(request, template_name='search.html', context=context)