"""
VIEWS
-----
ViewSets REST.
Cada ViewSet representa un endpoint CRUD o de solo lectura.
"""
#--------------------------------------------------------------------------------
# Importación de vistas de DRF, permisos y los modelos y serializers del app Herramental.
#--------------------------------------------------------------------------------
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import * #TipoHerramental, Herramental, Familia, estadoHerramental
from .serializers import * #TipoHerramentalSerializer, HerramentalSerializer, FamiliaSerializer, estadoHerramentalSerializer, HerramentalEspecificoSerializer
#Librerías para la clase de bajo nivel que recibe parámetros.
from rest_framework.views import APIView
from django.http.response import JsonResponse

#--------------------------------------------------------------------------------
# ViewSets CRUD para cada modelo definido.
# Cada ViewSet define el queryset, el serializer y los permisos (comentados por ahora).
#--------------------------------------------------------------------------------
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


# Add 27_01_2026
# Se realiza cambio de utilizando modelviewset a apiview para recibir parámetros. (validar efectividad y robustez.)
class estadoHerramentalViewSet(ModelViewSet):
    queryset = EstadoHerramental.objects.all()
    serializer_class = estadoHerramentalSerializer
    #permission_classes = [IsAuthenticated]


#CLASES BAJO NIVEL QUE RECIBEN PARÁMETROS.
# Imprementación de .as_view() (bajo nivel - viewset alto nivel)
class Clase2(APIView):

    def get(self, request, id):
        try:
            data = EstadoHerramental.objects.filter(id=id).get()
            return JsonResponse({"data": estadoHerramentalSerializer(data).data}, status=200)
        except EstadoHerramental.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)
        
        
# Implementación de ViewSet para HerramentalEspecifico con relaciones a estadoHerramental, Piso y Estanteria (05_03_2026)
# Se agrega también un ViewSet para DieSet, que es otra entidad relacionada con ubicaciones (13_03_2026).
class DieSetViewSet(ModelViewSet):
    queryset = DieSet.objects.all()
    serializer_class = DieSetSerializer


class HerramentalEspecificoViewSet(ModelViewSet):
    # Optimizamos la consulta usando select_related para TODAS las llaves foráneas
    # Esto hace un JOIN en SQL Server y trae todo en una sola petición.
    queryset = HerramentalEspecifico.objects.select_related(
        # --- Relaciones Directas (Nivel 1) ---
        'hesp_IdFamilia',
        'hesp_IdTipoHerramental',
        'hesp_IdEstadoHerr',
        'hesp_IdMaquinaPP',
        'hesp_IdMaquinaOpc',
        'hesp_IdActividad',
        #'hesp_IdImagen',
        'hesp_IdChatarrizacion',
        'hesp_IdOrdenProduccion',
        'hesp_IdPrestamo',
        'hesp_IdPiso',
        'hesp_IdEstanteria',
        'hesp_IdUbicacionHerr',
        
       # --- Relaciones Anidadas (Nivel 2) ---
        'hesp_IdDieSet',                 # El DieSet en sí
        'hesp_IdDieSet__di_IdPiso',       # El Piso que está dentro del DieSet
        'hesp_IdDieSet__di_IdEstanteria', # La Estantería dentro del DieSet
        'hesp_IdDieSet__di_IdUbicacionDieset' # La Ubicación dentro del DieSet
    ).all()
    serializer_class = HerramentalEspecificoSerializer
    