from django.shortcuts import render, get_object_or_404
from .models import Bill, BillItem, Customer
from num2words import num2words

def new_bill(request):
    customers = Customer.objects.all()
    return render(request, 'new_bill.html', {'customers': customers})

# def bills_list(request):
#     bills = Bill.objects.select_related('customer').all()
#     return render(request, "bill_list.html", {"bills": bills})

def bills_list(request):
    bills = Bill.objects.select_related('customer').all()
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        bills = bills.filter(
            Q(bill_number__icontains=search) | 
            Q(customer__name__icontains=search) |
            Q(customer__phone__icontains=search)
        )
    
    # Filter by payment status
    status = request.GET.get('status')
    if status:
        bills = bills.filter(payment_status=status)
    
    # Filter by date range
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if date_from:
        bills = bills.filter(date__date__gte=date_from)
    if date_to:
        bills = bills.filter(date__date__lte=date_to)
    
    # Sorting
    ordering = request.GET.get('ordering', '-date')  # Default sort by date descending
    if ordering:
        bills = bills.order_by(ordering)
    
    return render(request, "bill_list.html", {"bills": bills})



def bill_detail_htmx(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    rupees_in_words = num2words(int(bill.total_amount), to='cardinal', lang='en_IN').title()
    return render(request, "bill_detail_readonly.html", {"bill": bill, "rupees_in_words": rupees_in_words})