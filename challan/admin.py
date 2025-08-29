from django.contrib import admin
from .models import Challan, ChallanItem

class ChallanItemInline(admin.TabularInline):  # show items inside challan
    model = ChallanItem
    extra = 1

@admin.register(Challan)
class ChallanAdmin(admin.ModelAdmin):
    inlines = [ChallanItemInline]
    list_display = ("id", "challan_number", "customer", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("challan_number", "customer__name")

# Register ChallanItem separately if you also want it in admin
admin.site.register(ChallanItem)
