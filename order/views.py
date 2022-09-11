from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


class OrderView(APIView):
    def get(self, request, id=None):
        if id:
            order = get_object_or_404(Order, pk=id)
            serializer = OrderSerializer(order)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateOrderSerializer(
            data={**request.data, 'customer': request.user.id}
        )
        if serializer.is_valid():
            serializer.save()
            return Response("ENJOY!", status=status.HTTP_200_OK)
        else:
            return Response("SORRY!", status=status.HTTP_400_BAD_REQUEST)


class LineItemView(APIView):
    def get(self, request, id=None):
        if id:
            line_item = get_object_or_404(LineItem, pk=id)
            serializer = LineItemSerializer(line_item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        line_items = LineItem.objects.all()
        serializer = LineItemSerializer(line_items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
