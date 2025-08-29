from django.urls import path
from . import views, api_views

urlpatterns = [
    path('new_bill', views.new_bill, name='new_bill_page'),
    path('api/bills/create', api_views.create_bill, name='create_bill'),
]
