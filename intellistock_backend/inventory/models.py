from django.db import models

# Store Table
class Store(models.Model):
    store_location = models.CharField(max_length=255)

    def __str__(self):
        return self.store_location

# Category Table
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

# Vendor Table
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    vendor_contact_number = models.CharField(max_length=15)
    vendor_email = models.EmailField()
    vendor_address = models.TextField()

    def __str__(self):
        return self.vendor_name

# Item Table
class Item(models.Model):
    item_description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_on_hand = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="items")
    suggested_quantity_to_order = models.IntegerField(default=0)
    actual_quantity_to_order = models.IntegerField(default=0)

    def __str__(self):
        return self.item_description

# Daily Sales Table
class DailySales(models.Model):
    sales_date = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="daily_sales")
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    number_of_transactions = models.IntegerField()
    inventory_usage = models.DecimalField(max_digits=12, decimal_places=2)
    waste_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Sales for {self.sales_date}"

# Monthly Sales Table
class MonthlySales(models.Model):
    sales_date = models.DateField()
    quarter = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="monthly_sales")
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    average_sales = models.DecimalField(max_digits=12, decimal_places=2)
    profit_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_transactions = models.IntegerField()
    inventory_usage = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Monthly Sales for {self.sales_date}"

# Order Table
class Order(models.Model):
    order_date = models.DateField()
    expected_delivery_date = models.DateField()
    status = models.CharField(max_length=50)
    projected_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"

# OrderItem Table
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="order_items")
    suggested_quantity_to_order = models.IntegerField()
    actual_quantity_to_order = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def total_value(self):
        return self.unit_cost * self.actual_quantity_to_order

# Deliveries Table
class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="deliveries")
    invoice_number = models.CharField(max_length=255)
    quantity_ordered = models.IntegerField()
    quantity_received = models.IntegerField()
    expected_delivery_date = models.DateField()
    delivery_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Delivery {self.id}"
