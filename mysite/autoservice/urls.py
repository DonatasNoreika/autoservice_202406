from django.contrib import admin
from django.urls import path, include
from .views import (index,
                    cars)

urlpatterns = [
    path("", index, name="index"),
    path("cars/", cars, name="cars"),
]
