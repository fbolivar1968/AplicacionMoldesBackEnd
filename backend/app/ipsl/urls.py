from rest_framework.routers import DefaultRouter
from .views import OrdenProduccionForjaViewSet

# Definición del router y registro de los ViewSets
router = DefaultRouter()
router.register(r'ordenes-produccion-forja', OrdenProduccionForjaViewSet, basename='ordenproduccionforja') 

urlpatterns = router.urls