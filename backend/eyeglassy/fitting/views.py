from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
import re
import cv2
import dlib
import numpy as np
import django
# from . import fitting
from django.http import HttpResponse
import base64

from django.conf import settings
from product.models import Glasses

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()

output_path = 'crawling/image/output'


'''
def main(request):
    return render(request, "fitting/home.html")

def fitting_camera(request):
    return render(request, 'fitting/fitting_camera.html')

def fitting_result(request):
    # 예상된 결과를 보여주는 뷰 함수
    return render(request, 'fitting/fitting_result.html')
'''

def run_fitting(glasses_path, image_file):
    predictor_path = os.path.join(settings.BASE_DIR, 'fitting/models/shape_predictor_68_face_landmarks.dat')

    # 얼굴 인식기와 랜드마크 인식기 초기화
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    # 얼굴 이미지 불러오기 (views.py에서 리액트에서 받아옴.)
    face_img = cv2.imread(image_file)
    cv2.imshow('test', face_img)

    # 얼굴 인식
    faces = detector(face_img)
    print('@@@@@@@', faces)
    
    # 안경 이미지 불러오기
    glasses_img = cv2.imread(glasses_path, cv2.IMREAD_UNCHANGED)

    for face in faces:
        landmarks = predictor(face_img, face)

        left_eye = (landmarks.part(40).x, landmarks.part(40).y)
        right_eye = (landmarks.part(46).x, landmarks.part(46).y)

        # 눈 사이 각도 계산
        angle = np.rad2deg(np.arctan2(right_eye[1]-left_eye[1], right_eye[0]-left_eye[0]))

        # 안경 이미지 회전
        rotated_glasses = cv2.rotate(glasses_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        rotated_glasses = cv2.rotate(rotated_glasses, cv2.ROTATE_90_CLOCKWISE)
        M = cv2.getRotationMatrix2D((glasses_img.shape[1] / 2, glasses_img.shape[0] / 2), -angle, 1)
        rotated_glasses = cv2.warpAffine(rotated_glasses, M, (glasses_img.shape[1], glasses_img.shape[0]))

        # 안경 이미지 사이즈 조정
        eye_distance = np.sqrt((right_eye[1]-left_eye[1])**2 + (right_eye[0]-left_eye[0])**2)
        # scale_factor = eye_distance / rotated_sunglasses.shape[1] * 1.25
        scale_factor = eye_distance / rotated_glasses.shape[1] * 2
        resized_glasses = cv2.resize(rotated_glasses, (0,0), fx=scale_factor, fy=scale_factor)

        # 안경 이미지 위치 계산
        center_x = int((left_eye[0] + right_eye[0]) / 2) - int(left_eye[0] / 2)
        center_y = int((left_eye[1] + right_eye[1]) / 2) - int(resized_glasses.shape[0] / 2)

        # 안경 이미지 합성
        for i in range(resized_glasses.shape[0]):
            for j in range(resized_glasses.shape[1]):
                if resized_glasses[i,j,3] > 0:
                    # face_img[center_y+i,center_x+j,:] = resized_glasses[i,j,:3]
                    face_img[center_y+i,center_x+j,:] = resized_glasses[i,j,:3]

    # 이미지를 바이트로 변환
    _, encoded_img = cv2.imencode('.jpg', face_img)
    byte_img = encoded_img.tobytes()

    return byte_img



@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST'])
@csrf_exempt
def fitting_face(request, id):
    # 1) 리액트에서 받아온 안경 이미지, 안경 정보
    try:
        # image_file = request.FILES.get('image')
        image_file = request.FILES['image']
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    # 2) 리액트에서 받아온 안경 데이터에서 id 추출
    product_img = 'res' + str(id) + '.png'

    # 3) 해당 안경의 누끼 이미지 경로 저장
    glasses_path = os.path.join(settings.DEFAULT_DIR, output_path, product_img)
    # glasses_path = '../../crawling/image/output/res' + product_id + '.png'
    
    image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)

    with open(image_path, 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)

    # 이미지 위에 안경 이미지 붙여서 반환
    fitted_face = run_fitting(glasses_path, image_path) # fitting앱 경로, 누끼딴 안경 이미지 경로, 얼굴 이미지

    # product_id = re.sub(r'[^0-9]', '', product_id) # 3

    # 3) 해당 안경의 누끼 이미지 경로 저장
    # glasses_path = '../../crawling/image/output/res' + product_id + '.png'

    # 이미지 위에 안경 이미지 붙여서 반환
    # fitted_face = fitting.run_fitting(fitting_path, glasses_path, image_file) # fitting앱 경로, 누끼딴 안경 이미지 경로, 얼굴 
    
    response_data = {'result': 'success', 'message': '이미지 처리 완료'}
    return JsonResponse(response_data)
    # return Response({'fitted_face': fitted_face})
    # return JsonResponse({'image' : image_file})
    # return HttpResponse(image_file, content_type='image/jpeg')
    
    # # HttpResponse로 이미지 반환

    # response = HttpResponse(fitted_face, content_type='image/jpeg')
    # return response

