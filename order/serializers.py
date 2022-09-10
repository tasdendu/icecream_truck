from rest_framework import serializers
from .models import *
from item.serializers import ItemSerializer
from drf_writable_nested import WritableNestedModelSerializer


class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = LineItem
        fields = ('id', 'quantity', 'price', 'item')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    line_items = LineItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'line_items', 'order_date')

# Create serializers


class CreateLineItemSerializer(serializers.HyperlinkedModelSerializer):
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(read_only=True)

    class Meta:
        model = Item
        fields = ('quantity', 'item', 'price')

    def validate(self, data):
        if data['quantity'] > data['item'].quantity:
            raise serializers.ValidationError(
                {"quantity": "item is out of stock"})
        return data


class CreateOrderSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    line_items = CreateLineItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'line_items', 'user', 'created_at')
