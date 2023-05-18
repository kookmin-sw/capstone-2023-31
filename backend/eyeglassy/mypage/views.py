from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def setprofile(request):
    if request.user.is_authenticated:
        user = request.user

        # 사용자 정보 가져오기
        nickname = user.nickname
        email = user.email
        face_shape = user.face_shape
        
        response_data = {'success': True, 
                         'nickname': nickname,
                         'email': email,
                         'face_shape': face_shape,
                        }

        return Response(response_data)
    else:
        return Response({'success': False, 'message': '잘못된 접근입니다.'})
