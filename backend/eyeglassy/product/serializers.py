from rest_framework import serializers
from .models import Glasses

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'cost',
            'brand',
            'url',
            'image',
            'shape',
        )
        model = Glasses

class ProductShapeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'shape',
        )
        model = Glasses

class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name'
        )
        model = Glasses