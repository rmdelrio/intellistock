from rest_framework import serializers
from .models import Item, Order, OrderItem

# Serializers convert Django model instances to JSON and vice versa. 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'quantity_in_stock', 'reorder_level', 'perishable', 'expiration_date']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

