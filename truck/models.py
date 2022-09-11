from django.db import models

# Create your models here.


class Truck(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    @property
    def total_amount(self):
        return sum([item.total_amount() for item in self.items.all()])

    def __str__(self):
        return self.name
