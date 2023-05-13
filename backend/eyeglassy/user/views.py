from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout # 충돌 해결
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
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
        if user.check_password(password): #해쉬화 해서 저장했기 때문에 해당 함수가 필요
            # 인증 성공 시 로그인 처리
            auth_login(request, user)
            return JsonResponse({'success': True, 'message': user.nickname+'님 반갑습니다.'})
        else: #비밀번호가 틀릴 경우
            return JsonResponse({'success': False, 'message': '비밀번호가 일치하지 않습니다.'})
  

def check_login(request):
    if request.user.is_authenticated:
        return JsonResponse({'isLoggedIn': True})
    else:
        return JsonResponse({'isLoggedIn': False})


@api_view(['POST'])
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return Response({'success': True, 'message': '로그아웃 되었습니다.'})
    else:
        return Response({'success': False, 'message': '잘못된 접근입니다.'})


@api_view(['POST'])
def set_profile(request):
    if request.user.is_authenticated:
        user = request.user

        # 사용자 정보 가져오기
        nickname = user.nickname
        email = user.email
        face_shape = user.face_shape
        glasses = user.glasses

        response_data={'success': True, 'message': '마이페이지',
                       'nickname': nickname,
            'email': email,
            'face_shape': face_shape,
            'glasses': glasses

        }


        return Response(response_data)
    else:
        return Response({'success': False, 'message': '잘못된 접근입니다.'})


@ensure_csrf_cookie
@api_view(["POST"])
def edit_profile(request):
    print(">> 1")
    updated_nickname = request.data.get('nickname')
    last_password = request.data.get("lastpassword")
    updated_password = request.data.get('updatedpassword')

    if request.user.is_authenticated:
        print(">> 2")
        user = request.user
        print(">> 3")
        if user.check_password(last_password):
            print(">> 4")
            if hasattr(user, 'nickname'):
                user.nickname = updated_nickname
            else:
                print(">> 5")
                return JsonResponse({'success': False, 'message': 'User model does not have a "nickname" field.'})

            user.set_password(updated_password)
            user.save()
            print(">> 6")
            # The user will be logged out after password change.
            # So, re-authenticate the user and log them in again.
            new_user = authenticate(
                request, email=user.email, password=updated_password)
            print(">> 7")
            if new_user is not None:
                print(">> 8")
                auth_login(request, new_user)
                print(">> 9")
                return JsonResponse({'success': True, 'message': '정보를 변경했습니다.'})
            else:
                print(">> 10")
                return JsonResponse({'success': False, 'message': '인증 실패'})
        else:
            print(">> 11")
            return JsonResponse({'success': False, 'message': '비밀번호를 다시 입력하세요'})
    else:
        print(">> 12")
        return JsonResponse({'success': False, 'message': '인증되지 않은 사용자입니다.'})
