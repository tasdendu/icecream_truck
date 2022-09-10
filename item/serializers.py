from django.urls import path, include
from django.contrib.auth.models import User
from item.models import Item, Flavor
from rest_framework import serializers

# Serializers define the API representation.


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['email', 'username', 'first_name', 'last_name']


class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavor
        fields = ['id', 'name']
