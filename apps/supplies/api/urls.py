from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplyViewSet

router = DefaultRouter()
router.register(r'', SupplyViewSet)  # Registrar el ViewSet para la API de supplies

urlpatterns = [
    path('', include(router.urls)),
]
