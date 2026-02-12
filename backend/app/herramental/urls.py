""" Generación de rutas para la aplicación herramental. """

from os import path
from rest_framework.routers import DefaultRouter
from .views import Clase2, TipoHerramentalViewSet, HerramentalViewSet, FamiliaViewSet, estadoHerramentalViewSet
#Librerías para incluir rutas con viewsets.
from django.urls import path, include


# Definición de rutas automáticas para los ViewSets.
router = DefaultRouter()
router.register(r'tipo_herramental', TipoHerramentalViewSet)
router.register(r'herramental', HerramentalViewSet)
router.register(r'familia', FamiliaViewSet)
router.register(r'estado_herramental', estadoHerramentalViewSet)  # Add 27_01_2026


# Definición de rutas para .as_view() (reciben parámetros)
#urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('estado_herramental/<int:id>', Clase2.as_view()), # Usa .as_view()
]