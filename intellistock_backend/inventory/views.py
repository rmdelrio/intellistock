from rest_framework import viewsets, APIView
from rest_framework.response import Response
from .tensorflow_model.model import predict_quantity
from .models import Category, Vendor, Item, DailySales, MonthlySales, Order, OrderItem, Delivery
from .serializers import (
    CategorySerializer, VendorSerializer, ItemSerializer,
    DailySalesSerializer, MonthlySalesSerializer, OrderSerializer,
    OrderItemSerializer, DeliverySerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.select_related('category', 'vendor')
    serializer_class = ItemSerializer

class DailySalesViewSet(viewsets.ModelViewSet):
    queryset = DailySales.objects.all()
    serializer_class = DailySalesSerializer

class MonthlySalesViewSet(viewsets.ModelViewSet):
    queryset = MonthlySales.objects.all()
    serializer_class = MonthlySalesSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('vendor')
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related('order_id', 'order_item_item_id')
    serializer_class = OrderItemSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.select_related('order')
    serializer_class = DeliverySerializer

class SuggestedOrderQuantity(APIView):
    def post(self, request, format=None):
        item_id = request.data.get('item_id')
        item = Item.objects.get(id=item_id)
        
        data_point = [item.quantity_on_hand, item.unit_cost, item.vendor.lead_time_days, item.reorder_point]
        
        suggested_quantity = predict_quantity(data_point)
        
        return Response({"suggested_quantity": suggested_quantity})
