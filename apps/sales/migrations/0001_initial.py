# Generated by Django 5.1.1 on 2024-10-02 15:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='SalesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('shipping_district', models.CharField(max_length=100)),
                ('shipping_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('shipping_long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone_number', models.CharField(max_length=15)),
                ('products', models.JSONField(default=list)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clients')),
                ('sale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sales_info', to='sales.sales')),
            ],
            options={
                'db_table': 'sales_info',
            },
        ),
    ]
