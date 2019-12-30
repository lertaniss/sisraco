from rest_framework import serializers
from .models import Coordenadas, Paradas, Rotas, Onibus, DistanciasR, DistanciaTR
#from geojson_serializer.serializers import geojson_serializer

class CoordenadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenadas
        fields = '__all__'
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