from django.contrib import admin
from django.urls import path, include
from .views import (index,
                    cars,
                    car,
                    search,
                    register,
                    profile,
                    OrderListView,
                    OrderDetailView,
                    UserOrderListView,
                    UserOrderCreateView,
                    UserOrderUpdateView,
                    UserOrderDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("cars/", cars, name="cars"),
    path("cars/<int:car_id>", car, name="car"),
    path('search/', search, name="search"),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path("orders/", OrderListView.as_view(), name="orders"),
    path("userorders/", UserOrderListView.as_view(), name="user_orders"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="order"),
    path("userorders/new", UserOrderCreateView.as_view(), name="userorders_new"),
    path("userorders/<int:pk>/update", UserOrderUpdateView.as_view(), name="userorders_update"),
    path("userorders/<int:pk>/delete", UserOrderDeleteView.as_view(), name="userorders_delete"),
]
