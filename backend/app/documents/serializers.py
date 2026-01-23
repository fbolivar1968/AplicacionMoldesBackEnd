from rest_framework import serializers
from .models import Imagen

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