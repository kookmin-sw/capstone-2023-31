from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login # 충돌 해결
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password,check_password

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
    except:
        print("실패")
        return Response({'message': '잘못된 접근입니다'}, status=status.HTTP_400_BAD_REQUEST)

    # 사용자 생성
    user = User.objects.create(
        email=email, nickname=nickname, password=hashed_password)

    # 사용자 정보 반환
    return JsonResponse({'success': True, 'message': '회원가입이 완료되었습니다.'})



@api_view(['POST'])
def login(request):
    
    email = request.data.get("email")
    password = request.data.get('password')

    if not email or not password:  #빈칸이 존재할 경우
        return JsonResponse({'success': False, 'message': '빈칸을 입력해주세요'})

    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist: # 가입 정보가 없을 경우
        return JsonResponse({'success': False, 'message': '가입 정보가 존재하지 않습니다.'})

    if user is not None:
        if user.check_password(password):
            # 인증 성공 시 로그인 처리
            auth_login(request, user)
            return JsonResponse({'success': True, 'message': user.nickname+'님 반갑습니다.'})
        else: #비밀번호가 틀릴 경우
            return JsonResponse({'success': False, 'message': '비밀번호가 일치하지 않습니다.'})
  
