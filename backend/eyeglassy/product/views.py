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
from .serializers import PostSerializer



class ListPost(generics.ListCreateAPIView):
    queryset = Glasses.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateAPIView):
    queryset = Glasses.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})