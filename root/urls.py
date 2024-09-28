from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', include('apps.clients.urls')),  # Incluye las rutas de la aplicación `clients`
]
