""" Generación de rutas para la aplicación herramental. """

from rest_framework.routers import DefaultRouter
from .views import TipoHerramentalViewSet, HerramentalViewSet, FamiliaViewSet

# Definición de rutas automáticas para los ViewSets.
router = DefaultRouter()
router.register(r'tipo_herramental', TipoHerramentalViewSet)
router.register(r'herramental', HerramentalViewSet)
router.register(r'familia', FamiliaViewSet)

urlpatterns = router.urls