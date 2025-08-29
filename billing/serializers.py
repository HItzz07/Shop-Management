from rest_framework import serializers # type: ignore
from .models import Bill, BillItem, Customer
import uuid

class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
        fields = ["product", "quantity", "price", "amount"]
        read_only_fields = ["amount"]


class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True)
    class Meta:
        model = Bill
        fields = ["id", "customer", "items"]
    
    def create(self, validated_data):
        items_data = validated_data.pop("items")
        validated_data["total_amount"] = sum(item["quantity"] * item["price"] for item in items_data)
        validated_data["bill_number"] = f"Bill-{uuid.uuid4()}"
        bill = Bill.objects.create(**validated_data)
        for item in items_data:
            item["total"] = item["quantity"] * item["price"]
            BillItem.objects.create(bill=bill, **item)
        return bill
