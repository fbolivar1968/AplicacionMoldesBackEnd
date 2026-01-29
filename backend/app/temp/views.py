from rest_framework import viewsets
from .models import DataQRFile
from .serializers import DataQRFileSerializer

class DataQRFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DataQRFiles to be viewed or edited.
    """
    queryset = DataQRFile.objects.all()#.order_by('-fecha_hora') # Ordena por fecha descendente
    serializer_class = DataQRFileSerializer