from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientsViewSet

router = DefaultRouter()
router.register(r'', ClientsViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]
