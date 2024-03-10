# disaster/views.py
from rest_framework import viewsets
from .models import Alert, SOSRequest, Donation
from .serializers import AlertSerializer, SOSRequestSerializer, DonationSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

# Similar viewsets for SOSRequest and Donation




