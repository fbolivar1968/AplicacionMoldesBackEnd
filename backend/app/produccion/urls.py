from rest_framework.routers import DefaultRouter
from .views import MaquinaViewSet

router = DefaultRouter()
router.register(r'maquinas',MaquinaViewSet,basename='maquina')

urlpatterns = router.urls
