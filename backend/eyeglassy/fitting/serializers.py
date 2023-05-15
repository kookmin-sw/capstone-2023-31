from rest_framework import serializers
# from product.models import Glasses

class FittingResultSerializer(serializers.Serializer):
    fitted_face = serializers.CharField()

