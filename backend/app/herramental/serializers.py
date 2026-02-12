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