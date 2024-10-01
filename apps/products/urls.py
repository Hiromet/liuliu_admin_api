from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')  # Rutas para las categorías

urlpatterns = [
    path('', include(router.urls)),
]
