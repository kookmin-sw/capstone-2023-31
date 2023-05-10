from rest_framework import serializers

class ShapeResultSerializer(serializers.Serializer):
    predicted_shape = serializers.CharField()
