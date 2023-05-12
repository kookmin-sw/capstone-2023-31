from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token

from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings


def main(request):
    return render(request, 'main.html')

def fitting_camera(request):
    return render(request, 'fitting_camera.html')

def fitting_result(request):
    return render(request, 'fitting_result.html')


@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})
