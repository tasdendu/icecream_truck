from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(
        max_length=254, unique=True, null=False, db_index=True)
    phone = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name', 'username']

    def get_username(self):
        return self.email
