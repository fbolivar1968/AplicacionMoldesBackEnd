from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PisoViewSet, EstanteriaViewSet, UbicacionViewSet

router = DefaultRouter()
router.register(r'pisos', PisoViewSet)
router.register(r'estanterias', EstanteriaViewSet)
router.register(r'ubicaciones', UbicacionViewSet)  # Add this line for UbicacionHerramental

urlpatterns = [
    path('', include(router.urls)),
]