from api.models import User, Customer, Invoice, Revenue
from scripts.placeholder_data import users, customers, invoices, revenue

def seed():
    for user in users:
        User.objects.create(**user)
    for customer in customers:
        Customer.objects.create(**customer)
    for invoice in invoices:
        customer = Customer.objects.get(id=invoice["customer_id"])
        invoice["customer"] = customer
        Invoice.objects.create(**invoice)
    for revenue_month in revenue:
        Revenue.objects.create(**revenue_month)
