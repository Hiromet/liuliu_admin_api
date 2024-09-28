from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', include('apps.clients.api.urls')),
    path('api/productss/', include('apps.productss.api.urls')),
]
