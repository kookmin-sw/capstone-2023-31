from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

from .models import User


@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return Response({'csrfToken': get_token(request)})


@api_view(['POST'])
def register(request):
    try:
        # image_file = request.FILES['image']
        email = request.data.get("email")
        nickname = request.data.get('nickname')
        password = request.data.get('password')

        # 비밀번호를 해시하여 저장
        hashed_password = make_password(password)
        print("성공")
    except KeyError:
        print("실패")
        return Response({'message': '이미지 파일이 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 사용자 생성
    user = User.objects.create(
        email=email, nickname=nickname, password=hashed_password)

    # 사용자 정보 반환
    return JsonResponse({'success': True, 'message': '회원가입이 완료되었습니다.'})
