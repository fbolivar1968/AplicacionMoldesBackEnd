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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.services.graph_service import MicrosoftGraphService

# ViewSet de solo lectura para OrdenProduccionForja
class OrdenProduccionForjaViewSet(ReadOnlyModelViewSet):
    queryset = OrdenProduccionForja.objects.all()
    serializer_class = OrdenProduccionForjaSerializer
    #permission_classes = [IsAuthenticated]

class OpPdfView(APIView):

    def get(self, request, consecutivo):
        try:
            graph = MicrosoftGraphService()
            result = graph.search_op_pdf(consecutivo)

            if not result:
                return Response(
                    {"error": "PDF no encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(result)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )