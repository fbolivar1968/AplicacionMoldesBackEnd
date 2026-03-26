from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Imagen
from .serializers import DocumentoSerializer

class DocumentoUploadView(APIView):
    # Parsers necesarios para leer archivos desde multipart/form-data
    parser_classes = (MultiPartParser, FormParser)

    # NUEVO: Método para retornar todas las imágenes (GET)
    def get(self, request, *args, **kwargs):
        documentos = Imagen.objects.all()
        # many=True es vital para retornar una lista de objetos
        serializer = DocumentoSerializer(documentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# NUEVO: Vista para obtener detalles de una imagen específica por su ID
class DocumentoDetailView(APIView):
    """
    GET: Consulta una imagen específica por su ID (pk).
    """
    def get(self, request, pk, *args, **kwargs):
        # Busca la imagen o devuelve 404 si no existe
        imagen = get_object_or_404(Imagen, pk=pk)
        serializer = DocumentoSerializer(imagen)
        return Response(serializer.data, status=status.HTTP_200_OK)  