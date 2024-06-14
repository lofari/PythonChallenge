from rest_framework import serializers

from app.models import Infraccion, GenerarInformeRequest, Persona, Vehiculo


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class InfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        fields = '__all__'


class CrearInfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        fields = ['patente',
                  'timestamp',
                  'comentarios']


class GenerarInformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerarInformeRequest
        fields = ['email']
