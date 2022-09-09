from django.db import models
from django.contrib.auth.models import User
from truck.models import Truck

# Create your models here.


class Customer(User, models.Model):
    phone = models.CharField(max_length=100, unique=True)
    truck = models.ForeignKey(Truck, related_name='truck')
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'email']

    def get_username(self) -> str:
        return super().get_username()
