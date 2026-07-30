from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    Serializador para validar los datos recibidos en el endpoint de Login.
    """
    username = serializers.CharField(
        required=True,
        trim_whitespace=True,
        error_messages={'blank': 'El nombre de usuario es requerido.'}
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        trim_whitespace=False,
        error_messages={'blank': 'La contraseña es requerida.'}
    )
