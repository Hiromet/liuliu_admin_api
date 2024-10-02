from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Sales, SalesInfo
from .serializers import SalesSerializer, SalesInfoSerializer, SalesListSerializer
from apps.clients.models import Clients
from apps.products.models import Product

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def list(self, request, *args, **kwargs):
        sales = Sales.objects.all()
        serializer = SalesListSerializer(sales, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            sale = Sales.objects.get(order_id=pk)
            sales_info = sale.sales_info
            serializer = SalesInfoSerializer(sales_info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Sales.DoesNotExist:
            return Response({"message": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        method='post',
        operation_description="Create a new order",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'client_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the client'),
                'product_id': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of product IDs'
                )
            },
            required=['client_id', 'product_id']
        ),
        responses={
            201: openapi.Response(description="Order successfully created"),
            400: openapi.Response(description="Bad request"),
            404: openapi.Response(description="Client or product not found")
        }
    )
    @action(detail=False, methods=['post'], url_path='create-order')
    def create_order(self, request):
        order_data = request.data

        # Validate and get the client
        client_id = order_data.get('client_id')
        if not client_id:
            return Response({"message": "client_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Clients.objects.get(id=client_id)
        except Clients.DoesNotExist:
            return Response({"message": "Client not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get and validate the products
        product_ids = order_data.get('product_id')
        if not product_ids or not isinstance(product_ids, list):
            return Response({"message": "A list of product_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        products = []
        total = 0
        for product_id in product_ids:
            try:
                product = Product.objects.get(id=product_id)
                products.append(product)  # Collecting Product instances
                total += product.price
            except Product.DoesNotExist:
                return Response({"message": f"Product with ID {product_id} not found."}, status=status.HTTP_404_NOT_FOUND)

        # Create the Sales object with an automatic `order_id`
        sale = Sales.objects.create()

        # Create the SalesInfo instance
        sales_info = SalesInfo.objects.create(
            sale=sale,
            client=client,
            shipping_address=client.address,
            shipping_district=client.district,
            shipping_lat=client.lat,
            shipping_long=client.lng,
            contact_email=client.email,
            contact_phone_number=client.phone_number,
            total=total
        )

        # Set the products for the ManyToManyField
        sales_info.products.set(products)

        # Serialize and return the response with a success message
        serializer = SalesInfoSerializer(sales_info)
        return Response(
            {"message": f"Your order has been successfully created #{sale.order_id}.", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
