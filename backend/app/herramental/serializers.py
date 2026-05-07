"""
SERIALIZERS
-----------
Transformación de  modelos Django a 
JSON consumible por frontend.
"""
#--------------------------------------------------------------------------------
# Importación de serializers de DRF y los modelos del app Herramental.
#--------------------------------------------------------------------------------
from rest_framework import serializers
from .models import * #TipoHerramental, Herramental, Familia, estadoHerramental


#--------------------------------------------------------------------------------
# Serializers para cada modelo, utilizando ModelSerializer para generar automáticamente los campos basados en el modelo.
#--------------------------------------------------------------------------------
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


class estadoHerramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoHerramental
        fields = '__all__'
        
        
class estadoHerramentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoHerramental
        fields = ('id', 
                  'nombre', 
                  'descripcion')
        
#05_03_2026 - Add Serializer para HerramentalEspecifico con RELACIONES a estadoHerramental, Piso y Estanteria
#13_03_2026 - Add Serializer for DieSet with relationships to Piso and Estanteria, and custom field for location details.

class DieSetSerializer(serializers.ModelSerializer):
    nombre_piso = serializers.ReadOnlyField(source='piso.pi_NumeroPiso')
    
    class Meta:
        model = DieSet
        fields = '__all__'


#--------------------------------------------------------------------------------
# Clase serializer para HerramentalEspecifico, incluyendo campos adicionales para mostrar información relacionada de otras tablas (como nombres en lugar de IDs).
#--------------------------------------------------------------------------------
class HerramentalEspecificoSerializer(serializers.ModelSerializer):
    # Campos extra para ver nombres en lugar de IDs en el GET
    codigo_familia = serializers.ReadOnlyField(source='hesp_IdFamilia.fa_CodigoFamilia')
    nombre_familia = serializers.ReadOnlyField(source='hesp_IdFamilia.fa_NombreFamilia')
    nombre_estado_Herr = serializers.ReadOnlyField(source='hesp_IdEstadoHerr.eh_NombreEstado')
    nombre_maquina_pp = serializers.ReadOnlyField(source='hesp_IdMaquinaPP.ma_NombreMaquina')
    nombre_maquina_opc = serializers.ReadOnlyField(source='hesp_IdMaquinaOpc.ma_NombreMaquina')
    nombre_actividad = serializers.ReadOnlyField(source='hesp_IdActividad.ac_NombreActividad')
    nombre_tipo_herra = serializers.ReadOnlyField(source='hesp_IdTipoHerramental.th_NombreTipoHerramental')
    codigo_tipo_herra = serializers.ReadOnlyField(source='hesp_IdTipoHerramental.codigo')
    codigo_dieset = serializers.ReadOnlyField(source='hesp_IdDieSet.di_CodigoDieSet')
    nombre_herramental = serializers.ReadOnlyField(source='hesp_IdHerramental.he_NombreHerramental')
    descripcion_chatarrizacion = serializers.ReadOnlyField(source='hesp_IdChatarrizacion.ch_Descripcion', default=None)
    consecutivo_op = serializers.ReadOnlyField(source='hesp_IdOrdenProduccion.op_ConsecutivOp', default=None)    
    estado_prestamo = serializers.ReadOnlyField(source='hesp_IdPrestamo.pr_EstadoPrestamo', default=None)
    numero_piso = serializers.ReadOnlyField(source='hesp_IdPiso.pi_NumeroPiso', default=None)
    descripcion_piso = serializers.ReadOnlyField(source='hesp_IdPiso.pi_DescripcionPiso', default=None)
    nombre_estanteria = serializers.ReadOnlyField(source='hesp_IdEstanteria.es_NombreEstanteria', default=None)
    numero_fila = serializers.ReadOnlyField(source='hesp_IdUbicacionHerr.uh_NumeroFila', default=None)
    numero_columna = serializers.ReadOnlyField(source='hesp_IdUbicacionHerr.uh_NumeroColumna', default=None)
    numero_posicion = serializers.ReadOnlyField(source='hesp_IdUbicacionHerr.uh_NumeroPosicion', default=None)

    class Meta:
        model = HerramentalEspecifico
        #fields = '__all__'
        fields = [
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
                  'nombre_herramental',
                  'hesp_IdTipoHerramental',
                  'nombre_tipo_herra',
                  'codigo_tipo_herra',
                  'hesp_IdFamilia',
                  'codigo_familia',
                  'nombre_familia',
                  'hesp_IdMaquinaPP',
                  'nombre_maquina_pp',
                  'hesp_IdMaquinaOpc',
                  'nombre_maquina_opc',
                  'hesp_IdActividad',
                  'nombre_actividad',
                  'hesp_IdEstadoHerr',
                  'nombre_estado_Herr',      
                  'hesp_IdDieSet',
                  'codigo_dieset',
                  'hesp_IdChatarrizacion',
                  'descripcion_chatarrizacion',
                  'hesp_IdOrdenProduccion',
                  'consecutivo_op',
                  'hesp_IdPrestamo',
                  'estado_prestamo',
                  'hesp_IdPiso',
                  'numero_piso',
                  'descripcion_piso',
                  'hesp_IdEstanteria',
                  'nombre_estanteria',
                  'hesp_IdPlano', 
                  'hesp_IdPropiedadHerramental',
                  'hesp_IdPlano',
                  'hesp_IdManual',
                  'hesp_IdImagen',
                  'hesp_IdUbicacionHerr',
                  'numero_fila',
                  'numero_columna',
                  'numero_posicion']
        read_only_fields = ['hesp_IdHerramentalEspecifico']
        
