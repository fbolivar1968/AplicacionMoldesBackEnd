from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken

from app.usuarios.serializers import UsuarioReadSerializer
from .serializers import LoginSerializer
from .backends import UsuarioNegocioService


def _generar_tokens(usuario):
    """
    Construcción manual del RefreshToken y AccessToken sin depender
    de django.contrib.auth ni de la tabla 'token_blacklist_outstandingtoken'.
    """
    refresh = RefreshToken()
    refresh['user_id'] = usuario.id
    refresh['username'] = usuario.user
    refresh['nombre'] = f"{usuario.nombre} {usuario.apellido}"
    refresh['rol'] = usuario.tipo_usuario.nombre if usuario.tipo_usuario else None
    refresh['cargo'] = usuario.cargo.nombre if usuario.cargo else None

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(APIView):
    """
    Endpoint para autenticación de usuario sin depender de django.contrib.auth.
    POST /api/auth/login/
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        usuario = UsuarioNegocioService.authenticate(username=username, password=password)
        if not usuario:
            return Response(
                {'detail': 'Credenciales inválidas.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        tokens = _generar_tokens(usuario)
        user_data = UsuarioReadSerializer(usuario).data

        return Response({
            'tokens': tokens,
            'user': user_data
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
    Endpoint para cierre de sesión stateless.
    POST /api/auth/logout/
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        return Response(
            {'detail': 'Sesión cerrada correctamente.'},
            status=status.HTTP_205_RESET_CONTENT
        )


class MeView(APIView):
    """
    Endpoint para obtener los datos del usuario autenticado actual.
    GET /api/auth/me/
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if not request.user or not hasattr(request.user, 'id'):
            return Response(
                {'detail': 'Usuario no autenticado o token inválido.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = UsuarioReadSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
