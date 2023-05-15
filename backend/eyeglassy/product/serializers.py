from rest_framework import serializers
from .models import Glasses

class PostSerializer(serializers.ModelSerializer):
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