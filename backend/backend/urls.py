# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls), # Disabled: admin app requires auth_user table
    # Endpoints de autenticación JWT
    # POST /api/auth/login/    → obtener tokens
    # POST /api/auth/refresh/  → renovar access token
    # POST /api/auth/logout/   → invalidar refresh token
    # GET  /api/auth/me/       → datos del usuario autenticado
    path('api/', include('app.herramental.urls')),
    path('api/', include('app.ipsl.urls')),
    path('api/', include('app.produccion.urls')),
    path('api/', include('app.usuarios.urls')),
    path('api/', include('app.documents.urls')),
    path('api/', include('app.posicion.urls')),
    path('api/', include('app.temp.urls')),
    #path('api/', include('herramental.urls')), # Ruta para la aplicación herramental
    path('api/auth/', include('app.auth_app.urls')),
]
