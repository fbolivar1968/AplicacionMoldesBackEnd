"""
VIEWS
-----
ViewSets REST.
Cada ViewSet representa un endpoint CRUD o de solo lectura.
"""

# Django REST Framework imports.
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import OrdenProduccionForja
from .serializers import OrdenProduccionForjaSerializer


# ViewSet de solo lectura para OrdenProduccionForja
class OrdenProduccionForjaViewSet(ReadOnlyModelViewSet):
    queryset = OrdenProduccionForja.objects.all()
    serializer_class = OrdenProduccionForjaSerializer
    #permission_classes = [IsAuthenticated]
