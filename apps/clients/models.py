from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from .choices import DISTRICT_CHOICES  # Importa las opciones desde choices.py

class Clients(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    district = models.CharField(max_length=100, choices=DISTRICT_CHOICES)  # Nuevo campo para el distrito
    address = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    phone_number = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex='^\d{9}$', message='Phone number must be exactly 9 digits')],
        verbose_name="Phone Number"
    )
    email = models.EmailField(
        max_length=254,
        validators=[EmailValidator(message='Enter a valid email address')],
        verbose_name="Email",
        unique=True  # Evita duplicados
    )
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    lat = models.FloatField(null=True, blank=True, verbose_name="Latitude")  # Nuevo campo de latitud
    lng = models.FloatField(null=True, blank=True, verbose_name="Longitude")  # Nuevo campo de longitud

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
