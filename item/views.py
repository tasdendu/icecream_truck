from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Item, Flavor
from .serializers import *


class ItemView(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(Item, pk=id)
            serializer = ItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class FlavorView(APIView):
    def get(self, request, id=None):
        if id:
            flavor = get_object_or_404(Flavor, pk=id)
            serializer = FlavorSerializer(flavor)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        flavors = Flavor.objects.all()
        serializer = FlavorSerializer(flavors, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
