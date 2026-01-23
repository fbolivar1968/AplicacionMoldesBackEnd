"""
VIEWS
-----
ViewSets REST.
Cada ViewSet representa un endpoint CRUD o de solo lectura.
"""

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import TipoHerramental, Herramental, Familia
from .serializers import TipoHerramentalSerializer, HerramentalSerializer, FamiliaSerializer


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
