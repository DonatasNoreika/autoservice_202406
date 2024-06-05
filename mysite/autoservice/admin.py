from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine)

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date']
    inlines = [OrderLineInLine]

# Register your models here.
admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
