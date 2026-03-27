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
    #hesp_IdPiso = serializers.ReadOnlyField(source='hesp_IdPiso.pi_NumeroPiso')
    #hesp_IdEstanteria = serializers.ReadOnlyField(source='hesp_IdEstanteria.es_NombreEstanteria')
    #hesp_IdUbicacionHerr = serializers.SerializerMethodField()
    #nombre_familia = serializers.ReadOnlyField(source='hesp_IdFamilia.fa_NombreFamilia')
    nombre_familia = serializers.SerializerMethodField()

    class Meta:
        model = HerramentalEspecifico
        #fields = '__all__'
        fields = (
                  'hesp_IdHerramentalEspecifico',
                  'hesp_CodigoHerramental', 
                  'hesp_CodigoAlterno', 
                  'hesp_Descripcion1',  
                  'hesp_CantHerramental', 
                  'hesp_Observacion', 
                  'hesp_FechaReparacion', 
                  'hesp_A',
                  'hesp_B',
                  'hesp_C',
                  'hesp_D',
                  'hesp_E',
                  'hesp_F',
                  'hesp_G',
                  'hesp_H',
                  'hesp_I',
                  'hesp_J',
                  'hesp_T',
                  'hesp_IdHerramental',
                  'hesp_IdTipoHerramental',
                  'hesp_IdFamilia',
                  'nombre_familia',
                  'hesp_IdEstadoHerr',
                  'hesp_IdMaquinaPP',
                  'hesp_IdMaquinaOpc',
                  'hesp_IdActividad',
                  'hesp_IdPropiedadHerramental',
                  'hesp_IdPlano',
                  'hesp_IdManual',
                  'hesp_IdImagen',
                  'hesp_IdPlano',
                  'hesp_IdDieSet',
                  'hesp_IdChatarrizacion',
                  'hesp_IdOrdenProduccion',
                  'hesp_IdPrestamo',
                  'hesp_IdPiso',
                  'hesp_IdEstanteria',
                  'hesp_IdUbicacionHerr')
        read_only_fields = ['hesp_IdHerramentalEspecifico']
    def get_detalle_ubicacion(self, obj):
        if obj.hesp_IdUbicacionHerr is None:
            return None
        return f"F:{obj.hesp_IdUbicacionHerr.uh_NumeroFila} C:{obj.hesp_IdUbicacionHerr.uh_NumeroColumna} P:{obj.hesp_IdUbicacionHerr.uh_NumeroPosicion}"

    def get_nombre_familia(self, obj):
        # Verificamos si existe la relación y si tiene el atributo
        if obj.hesp_IdFamilia:
            return obj.hesp_IdFamilia.fa_NombreFamilia
        return "Sin Familia" # O None