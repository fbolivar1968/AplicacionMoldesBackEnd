from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrdenProduccionForjaViewSet, OpPdfView

# Definición del router y registro de los ViewSets
router = DefaultRouter()
router.register(r'ordenes-produccion-forja', OrdenProduccionForjaViewSet, basename='ordenproduccionforja') 

urlpatterns = [
    *router.urls,
    path('op-pdf/<int:consecutivo>/', OpPdfView.as_view(), name='op-pdf'),
]