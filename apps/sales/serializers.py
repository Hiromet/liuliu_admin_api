from rest_framework import serializers
from .models import Sales, SalesInfo
from apps.clients.serializers import ClientDetailSerializer
from apps.products.serializers import ProductSerializer

class ShippingInfoSerializer(serializers.Serializer):
    shipping_address = serializers.CharField()
    shipping_district = serializers.CharField()
    shipping_lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    shipping_long = serializers.DecimalField(max_digits=9, decimal_places=6)

class ContactInfoSerializer(serializers.Serializer):
    contact_email = serializers.EmailField()
    contact_phone_number = serializers.CharField()

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['id', 'order_id', 'sale_date']

class SalesListSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, source='sales_info.total')
    product_count = serializers.IntegerField(source='sales_info.products.count')

    class Meta:
        model = Sales
        fields = ['id', 'order_id', 'sale_date', 'total', 'product_count']

class SalesInfoSerializer(serializers.ModelSerializer):
    client = ClientDetailSerializer()  # Anidar el serializador de detalles del cliente
    products = ProductSerializer(many=True)  # Anidar el serializador de productos
    shipping_info = ShippingInfoSerializer(source='*')  # Extraer los campos relacionados con el envío
    contact_info = ContactInfoSerializer(source='*')  # Extraer los campos relacionados con el contacto

    class Meta:
        model = SalesInfo
        fields = [
            'id', 'sale', 'client', 'shipping_info', 'contact_info',
            'products', 'total'
        ]
