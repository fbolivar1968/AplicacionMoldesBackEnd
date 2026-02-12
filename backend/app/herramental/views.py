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
#Librerías para la clase de bajo nivel que recibe parámetros.
from rest_framework.views import APIView
from django.http.response import JsonResponse


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
# Se realiza cambio de utilizando modelviewset a apiview para recibir parámetros. (validar efectividad y robustez.)
class estadoHerramentalViewSet(ModelViewSet):
    queryset = estadoHerramental.objects.all()
    serializer_class = estadoHerramentalSerializer
    #permission_classes = [IsAuthenticated]


#--------------------------------------------------------------------------------------------------------------------------------------
#CLASES BAJO NIVEL QUE RECIBEN PARÁMETROS.

# Imprementación de .as_view() (bajo nivel - viewset alto nivel)

class Clase2(APIView):

    def get(self, request, id):
        try:
            data = estadoHerramental.objects.filter(id=id).get()
            return JsonResponse({"data": estadoHerramentalSerializer(data).data}, status=200)
        except estadoHerramental.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)