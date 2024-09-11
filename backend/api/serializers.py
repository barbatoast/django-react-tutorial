from rest_framework import serializers
from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "name", "email", "password"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ["id", "name", "email", "image_url"]

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = ["customer_id", "amount", "status", "date"]

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Revenue
        fields = ["month", "revenue"]
