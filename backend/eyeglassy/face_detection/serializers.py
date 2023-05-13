# [myproject]/[project_folder]/serializers.py를 만들어 줍니다.
# 아래의 의미는 방금 설치한 Djago REST framework를 import하여
# serializers를 통해 본인이 만들었던 모델(예를 들어 지금 예시에서는 'Mise'라는 model class)의
# 모든 필드에 대해 serializer하는 MiseSerializer을 생성한다 의미입니다.

from rest_framework import serializers
from .models import *


class MiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mise
        fields = '__all__'
