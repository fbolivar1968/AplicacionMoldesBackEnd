from rest_framework import serializers
from .models import Usuario, TipoUsuario, Cargo


class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ['id', 'nombre']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'nombre', 'area']   

class UsuarioSerializer(serializers.ModelSerializer):
    tipo_usuario = TipoUsuarioSerializer(read_only=True)
    cargo = CargoSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id',
            'cedula',
            'nombre',
            'apellido',
            'celular',
            'correo',
            'user',
            'password',
            'tipo_usuario',
            'cargo',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UsuarioReadSerializer(serializers.ModelSerializer):
    """
    Serializer de lectura (NO expone password).
    """
    tipo_usuario = TipoUsuarioSerializer(read_only=True)
    cargo = CargoSerializer(read_only=True)

    class Meta:
        model = Usuario
        exclude = ['password']