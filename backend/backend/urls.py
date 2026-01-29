from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.herramental.urls')),
    path('api/', include('app.ipsl.urls')),
    path('api/', include('app.produccion.urls')),
    path('api/', include('app.usuarios.urls')),
    path('api/', include('app.documents.urls')),
    path('api/', include('app.posicion.urls')),
    path('api/', include('app.temp.urls')),
]
