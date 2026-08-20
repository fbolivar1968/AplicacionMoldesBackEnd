from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Imagen, Plano, Manual
from .serializers import DocumentoSerializer, PlanoSerializer, ManualSerializer

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

class PlanoUploadView(APIView):
    # Parsers necesarios para leer archivos desde multipart/form-data
    parser_classes = (MultiPartParser, FormParser)

    # NUEVO: Método para retornar todos los planos (GET)
    def get(self, request, *args, **kwargs):
        planos = Plano.objects.all()
        # many=True es vital para retornar una lista de objetos
        serializer = PlanoSerializer(planos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = PlanoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PlanoDetailView(APIView):
    """
    GET: Consulta un plano específico por su ID (pk).
    """
    def get(self, request, pk, *args, **kwargs):
        # Busca el plano o devuelve 404 si no existe
        plano = get_object_or_404(Plano, pk=pk)
        serializer = PlanoSerializer(plano)
        return Response(serializer.data, status=status.HTTP_200_OK)  

class ManualUploadView(APIView):
    # Parsers necesarios para leer archivos desde multipart/form-data
    parser_classes = (MultiPartParser, FormParser)

    # NUEVO: Método para retornar todos los manuales (GET)
    def get(self, request, *args, **kwargs):
        manuales = Manual.objects.all()
        # many=True es vital para retornar una lista de objetos
        serializer = ManualSerializer(manuales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ManualSerializer(data=request.data)
        if serializer.is_valid():
            if 'usuario' not in serializer.validated_data or serializer.validated_data.get('usuario') is None:
                usuario = None
                if request.user and getattr(request.user, 'is_authenticated', False) and hasattr(request.user, 'id'):
                    usuario = request.user
                else:
                    from app.usuarios.models import Usuario
                    usuario = Usuario.objects.first()
                serializer.save(usuario=usuario)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ManualDetailView(APIView):
    """
    GET: Consulta un manual específico por su ID (pk).
    """
    def get(self, request, pk, *args, **kwargs):
        # Busca el manual o devuelve 404 si no existe
        manual = get_object_or_404(Manual, pk=pk)
        serializer = ManualSerializer(manual)
        return Response(serializer.data, status=status.HTTP_200_OK)  