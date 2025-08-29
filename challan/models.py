from django.db import models

# Create your models here.
from django.db import models
from billing.models import Customer, Product

class Challan(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    challan_number = models.CharField(max_length=20, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Challan {self.challan_number} - {self.customer.name}"


class ChallanItem(models.Model):
    challan = models.ForeignKey(Challan, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} ({self.challan.challan_number})"
