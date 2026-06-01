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
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max


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


#--------------------------------------------------------------------------------
# ENDPOINT: Siguiente consecutivo para HerramentalEspecifico
# GET /api/herramental/next-consecutive?h=<IdHerramental>&t=<IdTipoHerramental>&f=<IdFamilia>
#
# Replica la lógica SQL:
#   SELECT ISNULL(MAX(hesp_Consecutivo), 0) + 1 AS NextConsecutive
#   FROM HERRAMENTALESPECIFICO
#   WHERE hesp_IdHerramental = @IdH
#     AND hesp_IdTipoHerramental = @IdT
#     AND hesp_IdFamilia = @IdF
#
# Respuesta exitosa: { "nextValue": 3 }
# El frontend aplica .padStart(2, '0') para obtener "03".
#--------------------------------------------------------------------------------
class NextConsecutiveView(APIView):

    def get(self, request):
        # --- 1. Leer y validar los parámetros de la URL ---
        id_herramental    = request.query_params.get('h')
        id_tipo_herramental = request.query_params.get('t')
        id_familia        = request.query_params.get('f')

        # Los tres parámetros son obligatorios
        if not all([id_herramental, id_tipo_herramental, id_familia]):
            return Response(
                {
                    "error": "Los parámetros 'h' (herramental), 't' (tipo) y 'f' (familia) son requeridos."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validar que sean enteros para evitar inyección de datos inesperados
        try:
            id_herramental      = int(id_herramental)
            id_tipo_herramental = int(id_tipo_herramental)
            id_familia          = int(id_familia)
        except ValueError:
            return Response(
                {"error": "Los parámetros deben ser números enteros."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # --- 2. Ejecutar la consulta equivalente al SQL original ---
        # MAX(hesp_Consecutivo) sobre los registros que coincidan con la combinación.
        # Si no existe ningún registro, aggregate devuelve None → usamos 0 como fallback.
        resultado = HerramentalEspecifico.objects.filter(
            hesp_IdHerramental=id_herramental,
            hesp_IdTipoHerramental=id_tipo_herramental,
            hesp_IdFamilia=id_familia,
        ).aggregate(max_consec=Max('hesp_Consecutivo'))

        max_actual   = resultado['max_consec'] or 0   # ISNULL(..., 0)
        next_value   = max_actual + 1                 # + 1

        # --- 3. Devolver la respuesta ---
        return Response({"nextValue": next_value}, status=status.HTTP_200_OK)