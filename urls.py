# disaster/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, DonationViewSet
from .views import SOSRequestViewSet


router = DefaultRouter()
router.register(r'alerts', AlertViewSet)
router.register(r'sos-requests', SOSRequestViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Other URL patterns for your application
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add the following line to disable favicon requests
    path('favicon.ico', lambda x: HttpResponse(status=204)),
    # Your other URL patterns
]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('my_endpoint/', views.my_view, name='my_endpoint'),
    # Add more URL patterns as needed
]

from django.urls import path, include
urlpatterns = [
    path('disaster/', include('disaster.urls')),
    # Other URL patterns
]
