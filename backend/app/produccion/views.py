from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Maquina
from .serializers import MaquinaSerializer, MaquinaReadSerializer


class MaquinaViewSet(ModelViewSet):
    """
    Endpoint CRUD para MAQUINA.
    GET    → listado / detalle (serializer anidado)
    POST   → crear
    PUT    → actualizar
    DELETE → eliminar (si reglas lo permiten)
    """

    queryset = Maquina.objects.select_related(
        'estado',
        'tipo'
    ).all()

    #permission_classes = [IsAuthenticated]

    filter_backends = [
        #DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ['estado', 'tipo']
    search_fields = ['nombre', 'codigo', 'marca']
    ordering_fields = ['nombre', 'codigo', 'numero']
    ordering = ['nombre']

    def get_serializer_class(self):
        """
        Usa serializer anidado solo para lectura.
        """
        if self.action in ['list', 'retrieve']:
            return MaquinaReadSerializer
        return MaquinaSerializer
