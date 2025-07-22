from django.db import models

class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    country_of_operation = models.CharField(max_length=100)
    daily_sales_average = models.CharField(max_length=100)
    monthly_ads_budget = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method_issue = models.BooleanField(default=False)
    ad_account_issue = models.BooleanField(default=False)
    number_of_products = models.IntegerField()
    product_type = models.CharField(max_length=255)
    reason_for_contact = models.TextField()

    def __str__(self):
        return self.full_name
