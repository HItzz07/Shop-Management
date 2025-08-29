from django.shortcuts import render, get_object_or_404
from .models import Bill, BillItem, Customer
from num2words import num2words

def new_bill(request):
    customers = Customer.objects.all()
    return render(request, 'new_bill.html', {'customers': customers})

def bills_list(request):
    bills = Bill.objects.select_related('customer').all()
    return render(request, "bill_list.html", {"bills": bills})


def bill_detail_htmx(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    rupees_in_words = num2words(int(bill.total_amount), to='cardinal', lang='en_IN').title()
    return render(request, "bill_detail_readonly.html", {"bill": bill, "rupees_in_words": rupees_in_words})