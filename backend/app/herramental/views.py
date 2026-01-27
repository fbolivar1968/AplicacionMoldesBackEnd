"""
VIEWS
-----
ViewSets REST.
Cada ViewSet representa un endpoint CRUD o de solo lectura.
"""

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import TipoHerramental, Herramental, Familia, estadoHerramental
from .serializers import TipoHerramentalSerializer, HerramentalSerializer, FamiliaSerializer, estadoHerramentalSerializer


# ViewSets CRUD para cada modelo definido.
class TipoHerramentalViewSet(ModelViewSet):
    queryset = TipoHerramental.objects.all()
    serializer_class = TipoHerramentalSerializer
    #permission_classes = [IsAuthenticated]

class HerramentalViewSet(ModelViewSet):
    queryset = Herramental.objects.all()
    serializer_class = HerramentalSerializer
    #permission_classes = [IsAuthenticated]

class FamiliaViewSet(ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
    #permission_classes = [IsAuthenticated]

#-----------------------------------------------------------
# Add 27_01_2026
class estadoHerramentalViewSet(ModelViewSet):
    queryset = estadoHerramental.objects.all()
    serializer_class = estadoHerramentalSerializer
    #permission_classes = [IsAuthenticated]
