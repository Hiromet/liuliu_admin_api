from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # Verificar si el request contiene una lista de productos
        if isinstance(request.data, list):
            # Crear múltiples productos
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Crear un solo producto
            serializer = self.get_serializer(data=request.data)

        # Validar y guardar los productos
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Respuesta personalizada
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
