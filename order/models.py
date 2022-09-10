from django.db import models
from customer.models import Customer
from item.models import Item

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        ordering = ('order_date',)


class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
