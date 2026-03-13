"""
SERIALIZERS
-----------
Transformación de  modelos Django a 
JSON consumible por frontend.
"""

from rest_framework import serializers
from .models import * #TipoHerramental, Herramental, Familia, estadoHerramental

class TipoHerramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHerramental
        fields = '__all__'


class HerramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramental
        fields = '__all__'


class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = '__all__'

"""
class estadoHerramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = estadoHerramental
        fields = '__all__'
"""
class estadoHerramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = estadoHerramental
        fields = ('id', 
                  'nombre', 
                  'descripcion')
        
#--------------------------------------------------------------------------------

"""
class HerramentalEspecificoSerializer(serializers.ModelSerializer):
    # Atributos "aplanados" para el Frontend
    #nombre_estado = serializers.ReadOnlyField(source='estado.eh_NombreEstadoHrr')
    #numero_piso = serializers.ReadOnlyField(source='piso.pi_NumeroPiso')
    #nombre_estanteria = serializers.ReadOnlyField(source='estanteria.es_NombreEstanteria')

    class Meta:
        model = HerramentalEspecifico
        fields = '__all__' # Opcionalmente lista los campos que necesites
"""
#05_03_2026 - Add Serializer para HerramentalEspecifico con RELACIONES a estadoHerramental, Piso y Estanteria
#13_03_2026 - Add Serializer for DieSet with relationships to Piso and Estanteria, and custom field for location details.


class DieSetSerializer(serializers.ModelSerializer):
    # Campos extra para ver nombres en lugar de IDs en el GET
    nombre_piso = serializers.ReadOnlyField(source='piso.pi_NumeroPiso')
    
    class Meta:
        model = DieSet
        fields = '__all__'



class HerramentalEspecificoSerializer(serializers.ModelSerializer):
    # Campos informativos adicionales para el GET
    nombre_piso = serializers.ReadOnlyField(source='piso.pi_NumeroPiso')
    nombre_estanteria = serializers.ReadOnlyField(source='estanteria.es_NombreEstanteria')
    detalle_ubicacion = serializers.SerializerMethodField()

    class Meta:
        model = HerramentalEspecifico
        fields = '__all__'

    def get_detalle_ubicacion(self, obj):
        return f"F:{obj.ubicacion_herr.uh_NumeroFila} C:{obj.ubicacion_herr.uh_NumeroColumna} P:{obj.ubicacion_herr.uh_NumeroPosicion}"