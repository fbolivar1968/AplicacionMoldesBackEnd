from rest_framework import serializers
from .models import Imagen, Plano, Manual
from app.usuarios.models import Usuario

class DocumentoSerializer(serializers.ModelSerializer):
    # Mapeamos para que en Postman uses nombres simples
    archivo = serializers.FileField(source='ruta_relativa')
    nombre = serializers.CharField(source='nombre_imagen')
    descripcion = serializers.CharField(source='descripcion_imagen', required=False)

    class Meta:
        model = Imagen
        # Usamos los nombres definidos en el modelo arriba
        fields = ['id_imagen', 'archivo', 'nombre', 'descripcion', 'fecha_creacion']
        read_only_fields = ['id_imagen', 'fecha_creacion']

    def validate_archivo(self, value):
        limit = 5 * 1024 * 1024
        if value.size > limit:
            raise serializers.ValidationError('El archivo no debe exceder los 5MB.')
        return value

class PlanoSerializer(serializers.ModelSerializer):
    archivo = serializers.FileField(source='RutaRelativaPlano')
    nombre = serializers.CharField(source='NombrePlano')
    descripcion = serializers.CharField(source='DescripcionPlano', required=False)

    class Meta:
        model = Plano
        fields = ['IdPlano', 'archivo', 'nombre', 'descripcion', 'FechaCreacion']
        read_only_fields = ['IdPlano', 'FechaCreacion']

    def validate_archivo(self, value):
        limit = 50 * 1024 * 1024 # Permitiendo hasta 50MB para planos (suelen ser más pesados)
        if value.size > limit:
            raise serializers.ValidationError('El archivo de plano no debe exceder los 50MB.')
        return value


class ManualSerializer(serializers.ModelSerializer):
    archivo = serializers.FileField(source='RutaRelativaManual')
    nombre = serializers.CharField(source='NombreManual')
    id_usuario = serializers.PrimaryKeyRelatedField(
        source='usuario',
        queryset=Usuario.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Manual
        fields = ['IdManual', 'archivo', 'nombre', 'id_usuario', 'FechaCreacion']
        read_only_fields = ['IdManual', 'FechaCreacion']

    def validate_archivo(self, value):
        limit = 50 * 1024 * 1024 # Permitiendo hasta 50MB para manuales (suelen ser más pesados)
        if value.size > limit:
            raise serializers.ValidationError('El archivo de manual no debe exceder los 50MB.')
        return value