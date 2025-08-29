from django.db import models
import uuid
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Stock Keeping Unit
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)  # supports larger values
    stock = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=20, default="pcs")  # unit of measure
    reorder_level = models.PositiveIntegerField(default=5)  # for low stock alerts
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.product_id})"

class Bill(models.Model):
    PAYMENT_STATUS = [
        ("Unpaid", "Unpaid"),
        ("Paid", "Paid"),
        ("Partial", "Partial"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=20, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="Unpaid")
    due_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Bill {self.bill_number} - {self.customer.name}"

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, related_name="items", on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  # price per unit at sale time
    total = models.DecimalField(max_digits=12, decimal_places=2)  # quantity * price

    def __str__(self):
        return f"{self.product} x {self.quantity} ({self.bill.bill_number})"
    
    @property
    def amount(self):
        return self.quantity * self.price