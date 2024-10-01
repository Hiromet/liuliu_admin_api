from rest_framework import serializers
from .models import Product, Category

# Serializador para el modelo Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Campos del modelo Category

# Serializador para el modelo Product
class ProductSerializer(serializers.ModelSerializer):
    # Definimos el campo category como una clave foránea, relacionada con el modelo Category
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'category', 'quantity', 'price']  # Incluyendo todos los campos necesarios
