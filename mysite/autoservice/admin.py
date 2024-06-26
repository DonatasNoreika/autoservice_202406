from django.contrib import admin
from .models import (Car,
                     CarModel,
                     Service,
                     Order,
                     OrderLine,
                     OrderComment,
                     Profile)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class CarAdmin(admin.ModelAdmin):
    list_display = ['vin_code', 'client_name', 'car_model', 'license_plate']
    list_filter = ['client_name', 'car_model']
    search_fields = ['license_plate', 'vin_code']


class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    fields = ['service', 'qty']


class OrderCommentInLine(admin.TabularInline):
    model = OrderComment
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'client', 'date', 'deadline', 'total', 'status', 'is_overdue']
    inlines = [OrderLineInLine, OrderCommentInLine]
    list_editable = ['deadline', 'client', 'status']


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'service', 'qty', 'price']


# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Profile)

