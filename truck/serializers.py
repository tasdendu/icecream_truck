from rest_framework import serializers
from .models import Truck


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'name']
