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


class RandomProductSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id - 2
    
    class Meta:
        fields = (
            'id',
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