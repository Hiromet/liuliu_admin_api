from rest_framework import serializers
from ..models import Clients

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'firstname', 'lastname', 'address', 'phone_number', 'email', 'birthday']
