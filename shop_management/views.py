from django.shortcuts import render, get_object_or_404
from num2words import num2words

def dashboard(request):
    return render(request, 'dashboard.html')