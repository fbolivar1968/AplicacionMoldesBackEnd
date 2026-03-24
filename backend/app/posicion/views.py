from rest_framework import viewsets
from .models import Piso, Estanteria, UbicacionHerramental
from .serializers import PisoSerializer, EstanteriaSerializer, UbicacionSerializer

class PisoViewSet(viewsets.ModelViewSet):
    queryset = Piso.objects.all()
    serializer_class = PisoSerializer

class EstanteriaViewSet(viewsets.ModelViewSet):
    queryset = Estanteria.objects.all()
    serializer_class = EstanteriaSerializer
    
class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = UbicacionHerramental.objects.all()
    serializer_class = UbicacionSerializer