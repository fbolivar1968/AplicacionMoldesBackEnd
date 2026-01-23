from django.urls import path
from .views import DocumentoUploadView

urlpatterns = [
    # Este será el endpoint: /api/documentos/
    path('documents/', DocumentoUploadView.as_view(), name='documento-upload'),
]