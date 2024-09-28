from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import SupplySerializer
from ..models import Supply
from django.db.models import Sum


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Supply successfully created", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Supply successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

    # Vista personalizada para calcular el precio total
    @action(detail=False, methods=['get'], url_path='total-price')
    def total_price(self, request):
        total = Supply.objects.aggregate(total_price=Sum('price'))['total_price']
        supplies = self.get_queryset()
        serializer = self.get_serializer(supplies, many=True)
        return Response({
            "supplies": serializer.data,
            "total_price": total if total is not None else 0.0
        })
