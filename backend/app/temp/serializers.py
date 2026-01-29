from rest_framework import serializers
from .models import DataQRFile

class DataQRFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataQRFile
        fields = [
            'molde'
        ]#'__all__' # Incluye todos los campos del modelo en el JSON