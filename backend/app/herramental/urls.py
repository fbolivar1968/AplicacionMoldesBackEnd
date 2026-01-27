""" Generación de rutas para la aplicación herramental. """

from rest_framework.routers import DefaultRouter
from .views import TipoHerramentalViewSet, HerramentalViewSet, FamiliaViewSet, estadoHerramentalViewSet

# Definición de rutas automáticas para los ViewSets.
router = DefaultRouter()
router.register(r'tipo_herramental', TipoHerramentalViewSet)
router.register(r'herramental', HerramentalViewSet)
router.register(r'familia', FamiliaViewSet)
router.register(r'estado_herramental', estadoHerramentalViewSet)  # Add 27_01_2026

urlpatterns = router.urls