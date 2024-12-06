from django.db import models
from django.utils.timezone import now

# Category Model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

# Store Table
class Store(models.Model):
    store_location = models.CharField(max_length=255)

    def __str__(self):
        return self.store_location

# Vendor Model
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=255)
    vendor_contact_number = models.CharField(max_length=50)
    vendor_email = models.EmailField()
    vendor_address = models.TextField()
    vendor_lead_time_days = models.IntegerField()  # Vendor Lead Time
    vendor_minimum_order_quantity = models.IntegerField()

    def __str__(self):
        return self.vendor_name

# Item Model
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_on_hand = models.IntegerField()
    reorder_point = models.IntegerField(default=0)  # Optional
    perishability = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="items")
    suggested_quantity_to_order = models.IntegerField(default=0)
    actual_quantity_to_order = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically calculate total cost
        self.total_cost = self.quantity_on_hand * self.unit_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name

# Daily Sales Model
class DailySales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    sales_date = models.DateField(default=now)
    store_location = models.CharField(max_length=255)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    number_of_transactions = models.IntegerField()
    inventory_usage = models.DecimalField(max_digits=10, decimal_places=2)
    waste_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sales on {self.sales_date} - {self.store_location}"

# Monthly Sales Model
class MonthlySales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    date = models.DateField(default=now)
    quarter = models.IntegerField()
    store_location = models.CharField(max_length=255)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    average_sales = models.DecimalField(max_digits=12, decimal_places=2)
    profit_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_transactions = models.IntegerField()
    inventory_usage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Monthly Sales {self.date} - {self.store_location}"

# Order Model
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=now)
    expected_delivery_date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="orders")
    total_quantity_ordered = models.IntegerField()
    projected_value = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    total_cases_ordered = models.IntegerField()
    horizon_projected_sales = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_id} - {self.vendor.vendor_name}"

# OrderItem Model
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    order_item_item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="order_items")
    suggested_quantity_to_order = models.IntegerField(default=0)
    actual_quantity_to_order = models.IntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Order Item {self.order_item_id} for {self.order}"

# Delivery Model
class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="deliveries")
    delivery_date = models.DateField()
    invoice_number = models.CharField(max_length=50)
    quantity_ordered = models.IntegerField()
    quantity_received = models.IntegerField()
    expected_delivery_date = models.DateField()
    delivery_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Delivery {self.delivery_id} for Order {self.order}"

