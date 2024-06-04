from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    price = models.FloatField(verbose_name="Price")


class CarModel(models.Model):
    make = models.CharField(verbose_name="Make", max_length=50)
    model = models.CharField(verbose_name="Model", max_length=50)


class Car(models.Model):
    license_plate = models.CharField(verbose_name="License Plate", max_length=10)
    vin_code = models.CharField(verbose_name="VIN code", max_length=20)
    client_name = models.CharField(verbose_name="Client name", max_length=50)
    car_model = models.ForeignKey(to="CarModel", verbose_name="Car Model", on_delete=models.SET_NULL, null=True,
                                  blank=True)


class Order(models.Model):
    date = models.DateField(verbose_name="Date", auto_now_add=True)
    car = models.ForeignKey(to="Car", verbose_name="Car", on_delete=models.CASCADE)


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", verbose_name="Order", on_delete=models.CASCADE)
    service = models.ForeignKey(to="Service", verbose_name="Service", on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.IntegerField(verbose_name="Quantity")
