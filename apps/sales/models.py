from django.db import models
from apps.clients.models import Clients
from apps.products.models import Product
import uuid

class Sales(models.Model):
    order_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)  # Automatically generate a unique ID
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

class SalesInfo(models.Model):
    sale = models.OneToOneField(Sales, related_name='sales_info', on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    # Shipping information
    shipping_address = models.TextField(null=True, blank=True)
    shipping_district = models.CharField(max_length=100)
    shipping_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    shipping_long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Contact information
    contact_email = models.EmailField()
    contact_phone_number = models.CharField(max_length=15)

    # Products
    products = models.ManyToManyField(Product)  # Use ManyToManyField to relate to Product
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order ID: {self.sale.order_id}"
