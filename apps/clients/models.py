from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Clients(models.Model):
    firstname = models.CharField(max_length=50)  # Cambiado de name a first_name
    lastname = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex='^\d{9}$', message='Phone number must be 9 digits')]
    )
    email = models.EmailField(validators=[EmailValidator()])
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
