from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class CarAdmin(admin.ModelAdmin):
    list_display = ['vin_code', 'client_name', 'car_model', 'license_plate']
    list_filter = ['client_name', 'car_model']


class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date']
    inlines = [OrderLineInLine]


# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
