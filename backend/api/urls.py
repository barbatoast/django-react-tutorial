from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('customers', views.CustomerList.as_view()),
    path('invoices', views.InvoiceList.as_view()),
    path('revenue', views.RevenueList.as_view()),
    path('invoices/latest', views.LatestInvoices.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
