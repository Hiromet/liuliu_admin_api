from rest_framework import serializers
from .models import Clients

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'firstname', 'lastname', 'district', 'address', 'references', 'phone_number', 'email', 'birthday', 'lat', 'lng']
