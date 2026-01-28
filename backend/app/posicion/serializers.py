from rest_framework import serializers
from .models import Piso, Estanteria

class PisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piso
        fields = '__all__'

class EstanteriaSerializer(serializers.ModelSerializer):
    # Obtenemos el campo pi_NumeroPiso navegando por la relación 'piso'
    nombre_del_piso = serializers.ReadOnlyField(source='piso.pi_DescripcionPiso')

    class Meta:
        model = Estanteria
        fields = [
            'es_IdEstanteria', 
            'es_NombreEstanteria', 
            'piso',             # Devuelve el ID para el POST/PUT
            'nombre_del_piso'   # Devuelve el texto descriptivo para el GET
        ]