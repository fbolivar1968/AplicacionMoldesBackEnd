from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(
    r'usuarios',
    UsuarioViewSet,
    basename='usuario'
)

urlpatterns = router.urls


"""
Endpoints disponibles:
GET     /api/usuarios/
GET     /api/usuarios/{id}/
POST    /api/usuarios/
PUT     /api/usuarios/{id}/
DELETE  /api/usuarios/{id}/
"""