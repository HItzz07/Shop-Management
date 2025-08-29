# billing/forms.py
from django import forms
from .models import Bill, BillItem

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ["customer", "bill_number"]

class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillItem
        fields = ["product", "quantity", "price"]