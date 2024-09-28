from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Clients
from .serializers import ClientsSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

    def create(self, request, *args, **kwargs):
        is_multiple = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_multiple)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        message = "Clients successfully created" if is_multiple else "Client successfully created"
        return Response(
            {"message": message, "data": serializer.data},
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Client successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
