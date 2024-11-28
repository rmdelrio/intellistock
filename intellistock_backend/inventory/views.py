from django.shortcuts import render

# Use Django REST Framework views to define the API endpoints for creating, retrieving, updating, and deleting items. 
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from .models import Item, Order, OrderItem
from .serializers import ItemSerializer, OrderSerializer, OrderItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #permission_classes = [IsAuthenticated]  # Optional: Use if you want only authenticated users to access these APIs

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
