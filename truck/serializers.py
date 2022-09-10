from rest_framework import serializers
from .models import Truck


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'name']
