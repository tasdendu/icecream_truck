from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Customer


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name',
                  'email', 'username', 'phone', 'password']
