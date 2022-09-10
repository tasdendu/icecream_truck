from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


class CustomerView(APIView):
    def get(self, request, id=None):
        if id:
            customer = get_object_or_404(Customer, pk=id)
            serializer = Serializer(customer)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        customers = Customer.objects.all()
        serializer = Serializer(customers, many=True)
        # queryset = Customer.objects.all()
        # serializer_class = Serializer
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
