from django.contrib import admin
from django.urls import path, include
from .views import (index,
                    cars,
                    car)

urlpatterns = [
    path("", index, name="index"),
    path("cars/", cars, name="cars"),
    path("cars/<int:car_id>", car, name="car"),
]
