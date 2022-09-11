from rest_framework import serializers
from .models import *
from item.serializers import ItemSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class LineItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = LineItem
        fields = ('id', 'quantity', 'price', 'item')


class OrderSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'line_items', 'order_date')

# Create serializers


class CreateLineItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(read_only=True)

    class Meta:
        model = LineItem
        fields = ('quantity', 'item', 'price')

    def validate(self, data):
        if data['quantity'] > data['item'].quantity:
            raise serializers.ValidationError(
                {"quantity": "item is out of stock"})
        return data


class CreateOrderSerializer(WritableNestedModelSerializer):
    line_items = CreateLineItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'line_items', 'customer', 'order_date')
