from django.urls import path
from .views import DocumentoUploadView
#------------------------------ Para servir archivos multimedia en desarrollo ------------------#
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    # Este será el endpoint: /api/documentos/
    path('documents/', DocumentoUploadView.as_view(), name='documento-upload'),
]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""