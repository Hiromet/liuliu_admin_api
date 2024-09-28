from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Clients(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex='^\d{9}$', message='Phone number must be 9 digits')]
    )
    email = models.EmailField(validators=[EmailValidator()])
    birthday = models.DateField(null=True, blank=True)  # Nuevo campo de cumpleaños

    def __str__(self):
        return f'{self.name} {self.lastname}'
