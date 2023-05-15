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
from product.models import Glasses


fitting_path = os.path.join(settings.BASE_DIR, 'fitting')

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()



def run_fitting(fittting_path, glasses_path, image_file):
    # 외부 파이썬 파일 실행
    result = subprocess.run(
        ['python', 'fitting.py', fittting_path, glasses_path, image_file], capture_output=True, text=True)

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

'''
def main(request):
    return render(request, "fitting/home.html")

def fitting_camera(request):
    return render(request, 'fitting/fitting_camera.html')

def fitting_result(request):
    # 예상된 결과를 보여주는 뷰 함수
    return render(request, 'fitting/fitting_result.html')
'''

@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST'])
@csrf_exempt
def fitting_face(request, product_id):
    # 1) 리액트에서 받아온 안경 이미지
    try:
        image_file = request.FILES.get('image')
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)

    # with open(image_path, 'wb+') as destination:
    #     for chunk in image_file.chunks():
    #         destination.write(chunk)

    # 2) 리액트에서 받아온 안경 데이터에서 id 추출
    product_id = re.sub(r'[^0-9]', '', product_id) # 3

    # 3) 해당 안경의 누끼 이미지 경로 저장
    glasses_path = '../../crawling/image/output/res' + product_id + '.png'

    # 이미지 위에 안경 이미지 붙여서 반환
    fitted_face = fitting.run_fitting(fitting_path, glasses_path, image_file) # fitting앱 경로, 누끼딴 안경 이미지 경로, 얼굴 이미지

    # return Response({'fitted_face': fitted_face})
    return JsonResponse({'fitted_face': fitted_face})
