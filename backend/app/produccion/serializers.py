from rest_framework import serializers
from .models import Maquina, EstadoMaquina, TipoMaquina, Actividad


class EstadoMaquinaSerializer(serializers.ModelSerializer):
    """
    Serializer de solo lectura para el estado de la máquina.
    """
    class Meta:
        model = EstadoMaquina
        fields = ['id', 'nombre']


class TipoMaquinaSerializer(serializers.ModelSerializer):
    """
    Serializer de solo lectura para el tipo de máquina.
    """
    class Meta:
        model = TipoMaquina
        fields = ['id', 'nombre', 'descripcion']


class MaquinaSerializer(serializers.ModelSerializer):
    """
    Serializer base para CREATE / UPDATE.
    Usa IDs para relaciones (POST, PUT).
    """
    class Meta:
        model = Maquina
        fields = [
            'id',
            'numero',
            'nombre',
            'anio_instalacion',
            'marca',
            'capacidad',
            'codigo',
            'descripcion',
            'estado',
            'tipo',
        ]


class MaquinaReadSerializer(serializers.ModelSerializer):
    """
    Serializer de lectura.
    Devuelve estado y tipo como objetos anidados.
    """
    estado = EstadoMaquinaSerializer(read_only=True)
    tipo = TipoMaquinaSerializer(read_only=True)

    class Meta:
        model = Maquina
        fields = [
            'id',
            'numero',
            'nombre',
            'anio_instalacion',
            'marca',
            'capacidad',
            'codigo',
            'descripcion',
            'estado',
            'tipo',
        ]

#_--------------------------------------------------------------

class ActividadSerializer(serializers.ModelSerializer):
    """
    Serializer para la actividad.
    """
    class Meta:
        model = Actividad
        fields = '__all__'
        """[
            'id',
            'usuario',
            'fecha_creacion',
            'descripcion',
        ]"""