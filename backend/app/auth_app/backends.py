from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from app.usuarios.models import Usuario


class UsuarioNegocioService:

    @staticmethod
    def authenticate(username, password):
        try:
            usuario = Usuario.objects.select_related(
                'tipo_usuario',
                'cargo'
            ).get(user=username)

            if usuario.password == password:
                return usuario

        except Usuario.DoesNotExist:
            return None

        return None

    def get_user(self, user_id):
        """
        Recupera la instancia de Usuario dado su ID de clave primaria (us_IdUsuario).
        """
        try:
            return Usuario.objects.select_related('tipo_usuario', 'cargo').get(pk=user_id)
        except Usuario.DoesNotExist:
            return None


class UsuarioJWTAuthentication(JWTAuthentication):
    """
    Autenticador JWT personalizado para DRF que rescata el usuario directamente
    de la tabla 'USUARIO' de negocio en lugar de consultar 'auth_user'.
    """

    def get_user(self, validated_token):
        try:
            user_id = validated_token.get('user_id')
            if not user_id:
                raise InvalidToken("El token no contiene el identificador 'user_id'")
        except KeyError:
            raise InvalidToken("Token inválido o malformado")

        try:
            user = Usuario.objects.select_related('tipo_usuario', 'cargo').get(pk=user_id)
        except Usuario.DoesNotExist:
            raise AuthenticationFailed("Usuario no encontrado", code="user_not_found")

        return user
