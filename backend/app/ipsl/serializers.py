"""
SERIALIZERS
-----------
Transforman modelos Django a JSON consumible por frontend.
"""
from rest_framework import serializers
from .models import OrdenProduccionForja

class OrdenProduccionForjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProduccionForja
        fields = '__all__'
        #read_only_fields = fields