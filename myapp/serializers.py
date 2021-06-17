from rest_framework import serializers
from .models import Coordenadas, Paradas, Rotas, Onibus, DistanciasR, DistanciaTR
#from geojson_serializer.serializers import geojson_serializer


class CoordenadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenadas
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.cor_x = validated_data.get('cor_x', instance.cor_x)
        instance.cor_y = validated_data.get('cor_y', instance.cor_y)
        instance.cor_velocidade = validated_data.get(
            'cor_velocidade', instance.cor_velocidade)
        instance.cor_oni_codigo = validated_data.get(
            'cor_oni_codigo', instance.cor_oni_codigo)
        instance.save()
        return instance


class ParadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradas
        fields = "__all__"


class RotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rotas
        fields = "__all__"


class OnibusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onibus
        fields = "__all__"


class DistanciasRSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanciasR
        fields = "__all__"


class DistanciaTRSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanciaTR
        fields = "__all__"
