# disaster/models.py
from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    location = models.CharField(max_length=100)
    disaster_type = models.CharField(max_length=50)
    severity = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class SOSRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
