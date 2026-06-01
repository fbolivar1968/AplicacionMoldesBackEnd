"""
VIEWS
-----
ViewSets REST.
Cada ViewSet representa un endpoint CRUD o de solo lectura.
"""
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse


# ==============================================================================
# VIEWSETS CRUD
# ==============================================================================

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


class estadoHerramentalViewSet(ModelViewSet):
    queryset = EstadoHerramental.objects.all()
    serializer_class = estadoHerramentalSerializer
    #permission_classes = [IsAuthenticated]


class DieSetViewSet(ModelViewSet):
    queryset = DieSet.objects.all()
    serializer_class = DieSetSerializer


# ==============================================================================
# FUNCIÓN AUXILIAR — Construir código y calcular consecutivo
# ==============================================================================

def _construir_codigo(id_herramental, id_tipo, id_familia):
    """
    Construye el código alfanumérico de un HerramentalEspecifico y calcula
    el próximo consecutivo disponible para esa combinación.

    ─────────────────────────────────────────────────────────────
    ESTRUCTURA DEL CÓDIGO:
        {he_CodigoHerramental}{th_CodigoTipoHerramental}-{fa_CodigoFamilia}{consecutivo:02d}

    EJEMPLOS:
        Herramental: MOLDE      (M)
        Tipo:        ESTAMPADOR (E)
        Familia:     HEXAGONAL  (HX)
        → prefijo base = "ME-HX"
        → primer registro   → "ME-HX01"
        → segundo registro  → "ME-HX02"

        Herramental: COPA       (C)
        Tipo:        ESTAMPADOR (E)
        Familia:     TLLO EN T  (TET)
        → prefijo base = "CE-TET"
        → primer registro   → "CE-TET01"
    ─────────────────────────────────────────────────────────────

    Parámetros:
        id_herramental (int) : PK de Herramental
        id_tipo        (int) : PK de TipoHerramental
        id_familia     (int) : PK de Familia

    Retorna dict:
        codigo_herramental (str) : código del herramental        → "M"
        codigo_tipo        (str) : código del tipo               → "E"
        codigo_familia     (str) : código de la familia          → "HX"
        codigo_base        (str) : prefijo sin consecutivo       → "ME-HX"
        next_consecutivo   (int) : próximo número entero         → 1
        consecutivo_fmt    (str) : consecutivo con zfill(2)      → "01"
        codigo_completo    (str) : código final generado         → "ME-HX01"

    Lanza ValueError si algún ID no existe en la BD.
    """

    # ── 1. Resolver los tres catálogos desde la BD ──────────────────────────
    try:
        herramental = Herramental.objects.get(pk=id_herramental)
    except Herramental.DoesNotExist:
        raise ValueError(f"No existe un Herramental con id={id_herramental}.")

    try:
        tipo = TipoHerramental.objects.get(pk=id_tipo)
    except TipoHerramental.DoesNotExist:
        raise ValueError(f"No existe un TipoHerramental con id={id_tipo}.")

    try:
        familia = Familia.objects.get(pk=id_familia)
    except Familia.DoesNotExist:
        raise ValueError(f"No existe una Familia con id={id_familia}.")

    # ── 2. Obtener los códigos y limpiar espacios en blanco ─────────────────
    codigo_herramental = (herramental.he_CodigoHerramental or "").strip()
    codigo_tipo        = (tipo.th_CodigoTipoHerramental   or "").strip()
    codigo_familia     = (familia.fa_CodigoFamilia         or "").strip()

    if not codigo_herramental:
        raise ValueError(f"El Herramental id={id_herramental} no tiene código asignado.")
    if not codigo_tipo:
        raise ValueError(f"El TipoHerramental id={id_tipo} no tiene código asignado.")
    if not codigo_familia:
        raise ValueError(f"La Familia id={id_familia} no tiene código asignado.")

    # ── 3. Construir el prefijo base ─────────────────────────────────────────
    # Formato: {CodHerramental}{CodTipo}-{CodFamilia}
    # Ejemplo: "M" + "E" + "-" + "HX" = "ME-HX"
    codigo_base = f"{codigo_herramental}{codigo_tipo}-{codigo_familia}"

    # ── 4. Calcular el próximo consecutivo ───────────────────────────────────
    # Filtra todos los HerramentalEspecifico de esta combinación y extrae
    # el número al final de cada código para encontrar el máximo actual.
    #
    # Ejemplo con codigo_base = "ME-HX":
    #   "ME-HX01" → sufijo "01" → int = 1
    #   "ME-HX02" → sufijo "02" → int = 2
    #   MAX = 2 → next = 3 → código = "ME-HX03"
    registros = HerramentalEspecifico.objects.filter(
        hesp_IdHerramental=id_herramental,
        hesp_IdTipoHerramental=id_tipo,
        hesp_IdFamilia=id_familia,
    ).values_list('hesp_CodigoHerramental', flat=True)

    max_consec = 0
    for codigo in registros:
        if codigo and codigo.startswith(codigo_base):
            # Extrae solo la parte numérica al final
            sufijo = codigo[len(codigo_base):]
            if sufijo.isdigit():
                max_consec = max(max_consec, int(sufijo))

    next_consecutivo = max_consec + 1

    # ── 5. Armar el código completo ──────────────────────────────────────────
    # zfill(2): rellena con ceros a la izquierda hasta 2 dígitos
    # 1 → "01" | 9 → "09" | 10 → "10" | 99 → "99"
    consecutivo_fmt = str(next_consecutivo).zfill(2)
    codigo_completo = f"{codigo_base}{consecutivo_fmt}"

    return {
        "codigo_herramental" : codigo_herramental,   # "M"
        "codigo_tipo"        : codigo_tipo,           # "E"
        "codigo_familia"     : codigo_familia,        # "HX"
        "codigo_base"        : codigo_base,           # "ME-HX"
        "next_consecutivo"   : next_consecutivo,      # 1
        "consecutivo_fmt"    : consecutivo_fmt,       # "01"
        "codigo_completo"    : codigo_completo,       # "ME-HX01"
    }


# ==============================================================================
# HERRAMENTAL ESPECÍFICO — ViewSet con lógica de código y consecutivo
# ==============================================================================

class HerramentalEspecificoViewSet(ModelViewSet):
    """
    ViewSet CRUD para HerramentalEspecifico.

    Endpoints estándar:
        GET    /api/herramental_especifico/         → lista todos
        GET    /api/herramental_especifico/<id>/    → detalle
        PUT    /api/herramental_especifico/<id>/    → actualiza completo
        PATCH  /api/herramental_especifico/<id>/    → actualiza parcial
        DELETE /api/herramental_especifico/<id>/    → elimina

    Endpoint con lógica especial:
        POST   /api/herramental_especifico/         → crea con validación de código
    """
    queryset = HerramentalEspecifico.objects.select_related(
        'hesp_IdFamilia',
        'hesp_IdTipoHerramental',
        'hesp_IdEstadoHerr',
        'hesp_IdMaquinaPP',
        'hesp_IdMaquinaOpc',
        'hesp_IdActividad',
        'hesp_IdChatarrizacion',
        'hesp_IdOrdenProduccion',
        'hesp_IdPrestamo',
        'hesp_IdPiso',
        'hesp_IdEstanteria',
        'hesp_IdUbicacionHerr',
        'hesp_IdDieSet',
        'hesp_IdDieSet__di_IdPiso',
        'hesp_IdDieSet__di_IdEstanteria',
        'hesp_IdDieSet__di_IdUbicacionDieset',
    ).all()
    serializer_class = HerramentalEspecificoSerializer

    def create(self, request, *args, **kwargs):
        """
        POST /api/herramental_especifico/

        ┌─────────────────────────────────────────────────────┐
        │  FLUJO DE CREACIÓN                                  │
        │                                                     │
        │  1. Recibe los 3 IDs en el body del POST            │
        │  2. Genera el código: ME-HX01                       │
        │  3. Verifica que ese código NO exista ya (409)      │
        │  4. Inyecta el código en los datos                  │
        │  5. Guarda y responde 201 con metadata              │
        └─────────────────────────────────────────────────────┘

        Body esperado (ejemplo mínimo):
        {
            "hesp_IdHerramental"     : 1,
            "hesp_IdTipoHerramental" : 2,
            "hesp_IdFamilia"         : 5,
            "hesp_CantHerramental"   : 1,
            ... resto de campos opcionales ...
        }

        El campo hesp_CodigoHerramental NO debe enviarse desde el frontend
        — este endpoint lo genera automáticamente.
        """
        data = request.data.copy()

        # ── 1. Leer y validar los 3 IDs obligatorios ────────────────────────
        id_herramental = data.get('hesp_IdHerramental')
        id_tipo        = data.get('th_IdTipoHerramental')
        id_familia     = data.get('fa_IdFamilia')

        if not all([id_herramental, id_tipo, id_familia]):
            return Response(
                {
                    "error": (
                        "Los campos 'hesp_IdHerramental', 'hesp_IdTipoHerramental' "
                        "y 'hesp_IdFamilia' son obligatorios para generar el código."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            id_herramental = int(id_herramental)
            id_tipo        = int(id_tipo)
            id_familia     = int(id_familia)
        except (ValueError, TypeError):
            return Response(
                {"error": "Los IDs deben ser números enteros."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ── 2. Construir código y calcular consecutivo ───────────────────────
        try:
            info = _construir_codigo(id_herramental, id_tipo, id_familia)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        codigo_generado  = info['codigo_completo']   # "ME-HX01"
        next_consecutivo = info['next_consecutivo']  # 1

        # ── 3. Verificar que el código no exista ya en la tabla ──────────────
        # Esto protege contra condiciones de carrera (dos usuarios creando
        # simultáneamente) o cuando el frontend no consultó next-consecutive.
        if HerramentalEspecifico.objects.filter(
            hesp_CodigoHerramental=codigo_generado
        ).exists():
            return Response(
                {
                    "advertencia": (
                        f"El código '{codigo_generado}' ya existe en la base de datos. "
                        f"Consulta GET /api/herramental/next-consecutive?h={id_herramental}"
                        f"&t={id_tipo}&f={id_familia} para obtener el consecutivo actualizado."
                    ),
                    "codigo_existente"   : codigo_generado,
                    "proximo_disponible" : f"{info['codigo_base']}{str(next_consecutivo + 1).zfill(2)}",
                },
                status=status.HTTP_409_CONFLICT   # 409 = el recurso ya existe
            )

        # ── 4. Inyectar el código generado antes de guardar ──────────────────
        # Sobreescribimos hesp_CodigoHerramental con el valor calculado,
        # sin importar lo que haya enviado el frontend en ese campo.
        data['hesp_CodigoHerramental'] = codigo_generado

        # ── 5. Serializar, validar y guardar ─────────────────────────────────
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "mensaje"          : "Herramental creado exitosamente.",
                "codigo_generado"  : codigo_generado,       # "ME-HX01"
                "consecutivo"      : next_consecutivo,      # 1
                "consecutivo_fmt"  : info['consecutivo_fmt'],# "01"
                "desglose": {
                    # Útil para debug o para mostrarlo en el frontend
                    "herramental" : info['codigo_herramental'],  # "M"
                    "tipo"        : info['codigo_tipo'],          # "E"
                    "familia"     : info['codigo_familia'],       # "HX"
                    "base"        : info['codigo_base'],          # "ME-HX"
                },
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


# ==============================================================================
# ENDPOINT: Preview del código y siguiente consecutivo
#
# GET /api/herramental/next-consecutive?h=<id>&t=<id>&f=<id>
#
# El frontend llama esto cada vez que el usuario selecciona los 3 selectores
# para mostrar en tiempo real el código que se va a generar.
#
# Respuesta exitosa (200):
# {
#   "nextValue"       : 3,          ← entero para padStart del frontend
#   "codigo_completo" : "ME-HX03",  ← código completo listo para mostrar
#   "codigo_base"     : "ME-HX",    ← prefijo (útil para el formulario)
#   "consecutivo_fmt" : "03"        ← ya formateado con zfill(2)
# }
#
# Errores posibles:
#   400 → parámetros faltantes, no enteros, o IDs inexistentes en BD
# ==============================================================================

class NextConsecutiveView(APIView):

    def get(self, request):

        # ── 1. Leer parámetros de la URL ─────────────────────────────────────
        id_herramental = request.query_params.get('h')
        id_tipo        = request.query_params.get('t')
        id_familia     = request.query_params.get('f')

        if not all([id_herramental, id_tipo, id_familia]):
            return Response(
                {"error": "Los parámetros 'h' (herramental), 't' (tipo) y 'f' (familia) son requeridos."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            id_herramental = int(id_herramental)
            id_tipo        = int(id_tipo)
            id_familia     = int(id_familia)
        except ValueError:
            return Response(
                {"error": "Los parámetros deben ser números enteros."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ── 2. Delegar toda la lógica a _construir_codigo() ─────────────────
        try:
            info = _construir_codigo(id_herramental, id_tipo, id_familia)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # ── 3. Responder con todo lo que necesita el frontend ────────────────
        return Response(
            {
                "nextValue"       : info['next_consecutivo'],  # 3       (entero)
                "codigo_completo" : info['codigo_completo'],   # "ME-HX03"
                "codigo_base"     : info['codigo_base'],       # "ME-HX"
                "consecutivo_fmt" : info['consecutivo_fmt'],   # "03"
            },
            status=status.HTTP_200_OK
        )


# ==============================================================================
# CLASE DE BAJO NIVEL — Filtrar EstadoHerramental por id de path
# ==============================================================================

class Clase2(APIView):
    def get(self, request, id):
        try:
            data = EstadoHerramental.objects.filter(id=id).get()
            return JsonResponse({"data": estadoHerramentalSerializer(data).data}, status=200)
        except EstadoHerramental.DoesNotExist:
            return JsonResponse({"error": "No encontrado"}, status=404)