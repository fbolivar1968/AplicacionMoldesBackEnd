from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioReadSerializer


class UsuarioViewSet(ModelViewSet):
    """
    CRUD USUARIO.
    """

    queryset = Usuario.objects.select_related(
        'tipo_usuario',
        'cargo'
    )

    #permission_classes = [IsAuthenticated] solicitar autenticación

    filter_backends = [
        #DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['tipo_usuario', 'cargo']
    search_fields = ['nombre', 'apellido', 'cedula', 'user']
    ordering_fields = ['nombre', 'apellido', 'fecha_creacion']
    ordering = ['apellido']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UsuarioReadSerializer
        return UsuarioSerializer
