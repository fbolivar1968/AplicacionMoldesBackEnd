from rest_framework.routers import DefaultRouter
from .views import MaquinaViewSet, ActividadViewSet

router = DefaultRouter()
router.register(r'maquinas',MaquinaViewSet,basename='maquina')
router.register(r'actividades',ActividadViewSet,basename='actividad')

urlpatterns = router.urls
