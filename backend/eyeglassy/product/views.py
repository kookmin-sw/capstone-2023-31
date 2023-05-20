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
from .serializers import ProductSerializer, RandomProductSerializer

from django.forms.models import model_to_dict
import random


def process_shape(request, shape):
    if request.method == 'GET':
        # print('shape@@', shape)
        glasses_shape = Glasses.objects.filter(shape=shape)
        glasses_data = [model_to_dict(glass) for glass in glasses_shape]
        return JsonResponse({'glasses_shape': glasses_data}, safe=False)
    

def get_random_product(request):
    p#print("2")
    if request.method == 'GET':
        product_count = 16
        all_products = list(Glasses.objects.all())
        random_glasses = random.sample(all_products, product_count)
        glasses_data = [model_to_dict(glass, fields=['id']) for glass in random_glasses]
        return JsonResponse({'random_glasses': glasses_data}, safe=False)


class RandomListProduct(generics.ListAPIView):
    queryset = Glasses.objects.exclude(name__isnull=True).exclude(name__exact='').order_by('?')[:16]
    serializer_class = RandomProductSerializer


# 문자열 검색하면 그 문자열이 포함된 product list를 쭈르륵 반환해주기
class SearchProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('query', '')

        queryset = Glasses.objects.filter(name__icontains=search_query)

        return queryset

    
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