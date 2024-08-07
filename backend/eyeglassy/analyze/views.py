from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
import subprocess

from . import analyze
from django.conf import settings

static_path = os.path.join(settings.BASE_DIR, 'static')



def run_modeling(image_file):
    # 외부 파이썬 파일 실행
    result = subprocess.run(
        ['python', 'analyze.py', static_path, image_file], capture_output=True, text=True)

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
    return render(request, "analyze/main.html")


def upload(request):
    # 예상된 결과를 보여주는 뷰 함수
    return render(request, 'analyze/upload.html')


@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})


@api_view(['POST'])
@csrf_exempt
def analyze_face(request):
    try:
        image_file = request.FILES['image']
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    image_path = os.path.join(settings.STATIC_ROOT, image_file.name)

    with open(image_path, 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)

    predicted_shape = analyze.run_modeling(settings.STATIC_ROOT, image_path)
    print(predicted_shape)
    return Response({'predicted_shape': predicted_shape})

@api_view(["POST"])
def save_faceshape(request):
    face_shape = request.data.get("face_shape")

    if not face_shape: #얼굴형 넘어와야함
        return JsonResponse({'success': False, 'message': '얼굴형이 분석되지 않았습니다.'})

    
    request.user.face_shape=face_shape
    request.user.save()  # 모델 필드 값을 저장

    return JsonResponse({'success': True, 'message': '얼굴형 정보가 성공적으로 저장되었습니다.'})

