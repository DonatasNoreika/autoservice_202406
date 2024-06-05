from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date']

# Register your models here.
admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
