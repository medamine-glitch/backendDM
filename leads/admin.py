from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 
        'phone_number', 
        'country_of_operation',
        'daily_sales_average',
        'monthly_ads_budget',
        'payment_method_issue',
        'ad_account_issue',
        'number_of_products',
        'product_type'
    ]
    list_filter = [
        'country_of_operation',
        'payment_method_issue',
        'ad_account_issue',
        'product_type'
    ]
    search_fields = [
        'full_name',
        'phone_number',
        'country_of_operation',
        'product_type'
    ]
    list_per_page = 25
