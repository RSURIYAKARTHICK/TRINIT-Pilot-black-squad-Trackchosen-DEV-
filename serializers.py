# disaster/serializers.py
from rest_framework import serializers
from .models import Alert, SOSRequest, Donation


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

# Similar serializers for SOSRequest and Donation
