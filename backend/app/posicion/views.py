from rest_framework import viewsets
from .models import Piso, Estanteria
from .serializers import PisoSerializer, EstanteriaSerializer

class PisoViewSet(viewsets.ModelViewSet):
    queryset = Piso.objects.all()
    serializer_class = PisoSerializer

class EstanteriaViewSet(viewsets.ModelViewSet):
    queryset = Estanteria.objects.all()
    serializer_class = EstanteriaSerializer