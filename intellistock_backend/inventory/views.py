from django.shortcuts import render

# Use Django REST Framework views to define the API endpoints for creating, retrieving, updating, and deleting items. 
from rest_framework.viewsets import ModelViewSet
from .models import Item, Vendor, Order, OrderItem, DailySales, MonthlySales, Delivery, Category, Store
from .serializers import (
    ItemSerializer, VendorSerializer, OrderSerializer, OrderItemSerializer,
    DailySalesSerializer, MonthlySalesSerializer, DeliverySerializer, CategorySerializer, StoreSerializer
)

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class DailySalesViewSet(ModelViewSet):
    queryset = DailySales.objects.all()
    serializer_class = DailySalesSerializer

class MonthlySalesViewSet(ModelViewSet):
    queryset = MonthlySales.objects.all()
    serializer_class = MonthlySalesSerializer

class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer