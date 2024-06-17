from django.shortcuts import render, redirect
from .models import Service, Order, Car
from django.views.generic import (ListView,
                                  DetailView)
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import password_validation
from django.contrib.auth.forms import User


# Create your views here.

def index(request):
    services = Service.objects.all().count()
    orders = Order.objects.filter(status="d").count()
    cars = Car.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'services': services,
        'orders': orders,
        'cars': cars,
        'num_visits': num_visits,
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
    cars = Car.objects.filter(Q(client_name__icontains=query) | Q(car_model__make__icontains=query) | Q(
        car_model__model__icontains=query) | Q(license_plate__icontains=query) | Q(vin_code__icontains=query))
    context = {
        "cars": cars,
        "query": query,
    }
    return render(request, template_name='search.html', context=context)


class UserOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "user_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} already exists!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Email {email} already exists!')
                    return redirect('register')
                else:
                    try:
                        password_validation.validate_password(password)
                    except password_validation.ValidationError as e:
                        for error in e:
                            messages.error(request, error)
                        return redirect('register')

                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords does not match!')
            return redirect('register')
    return render(request, 'registration/register.html')
