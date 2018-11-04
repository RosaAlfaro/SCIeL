from .models import Cultivo, Etapa, Dispositivo, Invernadero, Parametro, Actuador, Sensor, Medicion
from rest_framework import serializers


class CultivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cultivo
        fields = (
            'id_cultivo',
            'nombre_cultivo',
            'periodo_cosecha'
        )
    

class EtapaSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Etapa
        fields = (
            'id_etapa',
            'id_cultivo',
            'numero_etapa',
            'nombre_etapa',
            'duracion',
            'descripcion_etapa'
        )
    

class DispositivoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dispositivo
        fields = (
            'id_dispositivo',
            'nombre_dispositivo'
        )


class InvernaderoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invernadero
        fields = (
            'id_invernadero',
            'id_dispositivo',
            'id_cultivo',
            'nombre_invernadero',
            'ubicacion'
        )


class ParametroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parametro
        fields = (
            'id_parametro',
            'id_invernadero',
            'nombre_parametro',
            'magnitud_referencia'
        )

class ActuadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actuador
        fields = (
            'id_actuador',
            'id_dispositivo',
            'id_invernadero',
            'nombre_actuador'
        )


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = (
            'id_sensor',
            'id_dispositivo',
            'id_invernadero',
            'nombre_sensor'
        )


class MedicionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicion
        fields = (
            'id_medicion',
            'id_invernadero',
            'id_parametro',
            'id_sensor',
            'id_actuador',
            'magnitud_medicion',
            'fecha_medicion',
            'is_activo'
        )
