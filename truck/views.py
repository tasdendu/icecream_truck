from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Truck
from .serializers import Serializer

# Create your views here.


class TruckView(APIView):
    def get(self, request, id=None):
        if id:
            truck = get_object_or_404(Truck, pk=id)
            serializer = Serializer(truck)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        trucks = Truck.objects.all()
        serializer = Serializer(trucks, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
