from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from catalogos.models import (
    Parentesco,
    Puesto
)
from catalogos.serializers import (
    ParentescoSerializer,
    PuestoSerializer
)

class ParentescoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ParentescoSerializer
    queryset = Parentesco.objects.all()
    
    @action(
        detail=False,
        methods=['get'],
        url_path="obtenerParentesco",
        permission_classes=[IsAuthenticatedOrReadOnly]
    )
    def obtenerParentesco(self, request):
        serial = self.serializer_class(self.queryset, many = True)
        return Response(serial.data, status=status.HTTP_200_OK)
    
class PuestoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = PuestoSerializer
    queryset = Puesto.objects.all()
    
    @action(
        detail=False,
        methods=['get'],
        url_path="obtenerPuesto",
        permission_classes=[IsAuthenticatedOrReadOnly]
    )
    def obtenerPuesto(self, request):
        serial = self.serializer_class(self.queryset, many = True)
        return Response(serial.data, status=status.HTTP_200_OK)