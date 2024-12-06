from rest_framework import serializers
from .models import Category, Vendor, Item, DailySales, MonthlySales, Order, OrderItem, Delivery

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'category_description']

# Vendor Serializer
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendor_id', 'vendor_name', 'vendor_contact_number', 'vendor_email', 'vendor_address', 'vendor_lead_time_days', 'vendor_minimum_order_quantity']

# Item Serializer
class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    vendor_name = serializers.CharField(source='vendor.vendor_name', read_only=True)

    class Meta:
        model = Item
        fields = [
            'item_id', 'item_name', 'item_description', 'category', 'category_name',
            'unit_cost', 'quantity_on_hand', 'reorder_point', 'perishability',
            'vendor', 'vendor_name', 'suggested_quantity_to_order', 'actual_quantity_to_order', 'last_updated'
        ]

# Daily Sales Serializer
class DailySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySales
        fields = [
            'sales_id', 'sales_date', 'store_location', 'total_sales',
            'number_of_transactions', 'inventory_usage', 'waste_amount'
        ]

# Monthly Sales Serializer
class MonthlySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlySales
        fields = [
            'sales_id', 'date', 'quarter', 'store_location', 'total_sales',
            'average_sales', 'profit_percentage', 'number_of_transactions', 'inventory_usage'
        ]

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)

    class Meta:
        model = Order
        fields = [
            'order_id', 'order_date', 'expected_delivery_date', 'vendor', 'vendor_name',
            'total_quantity_ordered', 'projected_value', 'status',
            'total_cases_ordered', 'horizon_projected_sales'
        ]

# Order Item Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.item_name', read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'order_item_id', 'order_id', 'item', 'item_name', 'suggested_quantity_to_order',
            'actual_quantity_to_order', 'unit_cost', 'total_value'
        ]

# Delivery Serializer
class DeliverySerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(source='order.order_id', read_only=True)

    class Meta:
        model = Delivery
        fields = [
            'delivery_id', 'order', 'order_id', 'delivery_date', 'invoice_number',
            'quantity_ordered', 'quantity_received', 'expected_delivery_date', 'delivery_status', 'total_cost'
        ]
