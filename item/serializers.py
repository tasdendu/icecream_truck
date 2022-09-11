from item.models import Item, Flavor
from rest_framework import serializers
from truck.serializers import Serializer

# Serializers define the API representation.


class ItemSerializer(serializers.ModelSerializer):
    truck = Serializer()

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'price', 'truck', 'total_amount']


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ['id', 'name']
