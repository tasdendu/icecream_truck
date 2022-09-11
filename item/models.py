from django.db import models
from truck.models import Truck
from django.db.models import Sum, F

# Create your models here.


class Flavor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    truck = models.ForeignKey(
        Truck, null=False, related_name="items", on_delete=models.CASCADE)
    flavors = models.ManyToManyField(Flavor, blank=False)

    def total_amount(self):
        return self.line_items.aggregate(total_amount=Sum(
            F('quantity')*F('price')))['total_amount']

    def __str__(self):
        return self.name
