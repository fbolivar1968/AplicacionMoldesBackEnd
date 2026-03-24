from rest_framework.routers import DefaultRouter
from django.db import router
from django.urls import path
from .views import DocumentoUploadView
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
    


urlpatterns = [
    # Endpoint: /api/documents/
    path('documents/', DocumentoUploadView.as_view(), name='documento-upload'),
]

# ESTO ES VITAL: Permite que el frontend pueda ver la imagen usando la URL devuelta
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)