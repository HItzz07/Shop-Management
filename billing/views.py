from django.shortcuts import render, redirect
from .models import Bill, BillItem, Customer

def new_bill(request):
    customers = Customer.objects.all()
    return render(request, 'new_bill.html', {'customers': customers})