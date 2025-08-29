from django.urls import path
from . import views, api_views

urlpatterns = [
    # View Urls
    path('new_bill', views.new_bill, name='new_bill_page'),
    path('bills/', views.bills_list, name='bills_list'),
    path('bills/<int:pk>/detail/', views.bill_detail_htmx, name='bill_detail_htmx'),
    # API Urls
    path('api/bills/create', api_views.create_bill, name='create_bill'),
]
