from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework import generics
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import Glasses
from .serializers import ProductSerializer

def process_shape(request):
    if request.method == 'GET':
        shape = request.GET.get('shape')
        glasses_shape = Glasses.objects.filter(shape=shape) # 특정 shape 인 안경 정보 반환
    return JsonResponse({'glasses_shape': glasses_shape})

class ListProduct(generics.ListAPIView):
    queryset = Glasses.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveAPIView):
    queryset = Glasses.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})