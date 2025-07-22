from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_lead, name='submit_lead'),
    path('lead/<int:pk>/', views.lead_detail, name='lead_detail'),
]
