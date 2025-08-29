from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Product, Bill, BillItem

class BillItemInline(admin.TabularInline):  # show items inside bill
    model = BillItem
    extra = 1

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    inlines = [BillItemInline]
    list_display = ("id", "customer", "date", "total_amount")

@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "price", "total")

admin.site.register(Customer)
admin.site.register(Product)
# admin.site.register(BillItem)
