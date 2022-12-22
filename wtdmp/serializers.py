from rest_framework import serializers
from .models import XD
from .models import Package

class XDSerializer(serializers.ModelSerializer):
    class Meta:
        model = XD
        fields = ['id', 'lat', 'lng']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'lat', 'lng']