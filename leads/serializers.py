
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            'id',
            'full_name',
            'phone_number',
            'country_of_operation',
            'daily_sales_average',
            'monthly_ads_budget',
            'payment_method_issue',
            'ad_account_issue',
            'number_of_products',
            'product_type',
            'reason_for_contact'
        ]