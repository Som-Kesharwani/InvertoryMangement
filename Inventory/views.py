from django.shortcuts import render
from .serializers import SalesSerializer, PurchaseSerialiser
from rest_framework import viewsets
from rest_framework import permissions
from .models import Sales, Purchase
# Create your views here.

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [permissions.IsAuthenticated]

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialiser
    permission_classes = [permissions.IsAuthenticated]
