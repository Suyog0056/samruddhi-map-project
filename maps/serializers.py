from rest_framework import serializers
from .models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class TalukaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taluka
        fields = '__all__'

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'

class VillageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageData
        fields = '__all__'
