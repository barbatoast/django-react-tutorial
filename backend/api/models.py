from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()

class Customer(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    image_url = models.URLField()

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.TextField()
    date = models.DateField()

class Revenue(models.Model):
    month = models.TextField()
    revenue = models.IntegerField()
