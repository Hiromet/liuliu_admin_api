from django.db import models


class Supply(models.Model):
    BOX = 'box'
    UNIT = 'unit'
    BAG = 'bag'
    LITER = 'liter'
    KILO = 'kilo'

    TYPE_CHOICES = [
        (BOX, 'Box'),
        (UNIT, 'Unit'),
        (BAG, 'Bag'),
        (LITER, 'Liter'),
        (KILO, 'Kilo'),
    ]

    product_name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
