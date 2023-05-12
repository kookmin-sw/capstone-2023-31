from django.shortcuts import render
from django.http import JsonResponse

from .models import User


@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})


def signup(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        password = request.POST['password']
        
