from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PisoViewSet, EstanteriaViewSet

router = DefaultRouter()
#router.register(r'pisos', PisoViewSet)
router.register(r'estanterias', EstanteriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]