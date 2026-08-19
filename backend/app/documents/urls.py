from rest_framework.routers import DefaultRouter
from django.db import router
from django.urls import path
from .views import (
    DocumentoDetailView,
    DocumentoUploadView,
    PlanoDetailView,
    PlanoUploadView,
    ManualDetailView,
    ManualUploadView
)
from django.conf import settings
from django.conf.urls.static import static
#------------------------------ Para servir archivos multimedia en desarrollo ------------------#
#from django.conf import settings
#from django.conf.urls.static import static
#router = DefaultRouter()
#router.register(r'documents', DocumentoUploadView, basename='documento-upload')

"""
urlpatterns = [
    # Este será el endpoint: /api/documentos/
    path('documents/', DocumentoUploadView.as_view(), name='documento-upload'),
]
"""
"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""
    


"""urlpatterns = [
    # Endpoint: /api/documents/
    path('documents/', DocumentoUploadView.as_view(), name='documento-upload'),
]"""


urlpatterns = [
    # 1. IMÁGENES (Tabla: IMAGEN)
    # URL: /api/documents/
    path('documents/', DocumentoUploadView.as_view(), name='documento-list-upload'),
    path('documents/<int:pk>/', DocumentoDetailView.as_view(), name='documento-detail'),

    # 2. PLANOS (Tabla: PLANO)
    # URL: /api/planos/
    path('documents/planos/', PlanoUploadView.as_view(), name='plano-list-create'),
    path('documents/planos/<int:pk>/', PlanoDetailView.as_view(), name='plano-detail'),

    # 3. MANUALES (Tabla: MANUAL)
    # URL: /api/manuales/
    path('documents/manuales/', ManualUploadView.as_view(), name='manual-list-create'),
    path('documents/manuales/<int:pk>/', ManualDetailView.as_view(), name='manual-detail'),
]

# Servir archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
