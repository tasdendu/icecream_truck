from django.db import models
from customer.models import Customer
from item.models import Item
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order_date']


class LineItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='line_items', blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    class Meta:
        unique_together = ['order', 'item']


@receiver(post_save, sender=LineItem)
def update_item(sender, **kwargs):
    line_item = kwargs['instance']
    item = line_item.item
    LineItem.objects.filter(id=line_item.id).update(price=item.price)
    Item.objects.filter(id=item.id).update(
        quantity=item.quantity - line_item.quantity)
