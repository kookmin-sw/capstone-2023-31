from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
import subprocess
import re
import django

from . import fitting
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from product.models import Glasses



static_path = os.path.join(settings.BASE_DIR, 'media')


def run_fitting(static_path, image_file, eyeglassy_num):
    # 외부 파이썬 파일 실행
    result = subprocess.run(
        ['python', 'fitting.py', static_path, image_file, eyeglassy_num], capture_output=True, text=True)

    # 실행 결과 확인
    output = result.stdout
    error = result.stderr

    if result.returncode == 0:
        # 실행이 성공적으로 완료됨
        print("외부 파이썬 파일 실행 결과:", output)
        return output
    else:
        # 실행 중 오류가 발생함
        print("오류 발생:", error)


def main(request):
    return render(request, "fitting/home.html")

def fitting_camera(request):
    return render(request, 'fitting/fitting_camera.html')

def fitting_result(request):
    # 예상된 결과를 보여주는 뷰 함수
    return render(request, 'fitting/fitting_result.html')


@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST'])
@csrf_exempt
def fitting_face(request):
    try:
        image_file = request.FILES.get('image') # 이미지 리액트에서 받아오기
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)

    with open(image_path, 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)

   
    # 해당 안경 이미지 정보 리액트에서 받아오기
    eyeglassy_num = request.FILES.get('char') # img3.jpg
    eyeglassy_num = re.sub(r'[^0-9]', '', eyeglassy_num) # 3

    # 이미지 위에 안경 이미지 붙여서 반환
    fitted_face = fitting.run_fitting(static_path, image_path, eyeglassy_num) # 안경 씌운 이미지 경로

    # return Response({'fitted_face': fitted_face})
    return JsonResponse({'fitted_face': fitted_face})
