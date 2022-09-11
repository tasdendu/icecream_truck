from item.models import Item, Flavor
from rest_framework import serializers

# Serializers define the API representation.


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['email', 'username', 'first_name', 'last_name']


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ['id', 'name']
