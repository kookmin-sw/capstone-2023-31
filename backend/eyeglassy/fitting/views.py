from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
import cv2
import dlib
import numpy as np
# from . import fitting
from django.http import HttpResponse
import base64

from django.conf import settings
from product.models import Glasses

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()

output_path = 'crawling/image/output'
model_path = 'fitting/models/shape_predictor_68_face_landmarks.dat'


def run_fitting(glasses_path, image_file):
    predictor_path = os.path.join(settings.BASE_DIR, model_path)

    # 얼굴 인식기와 랜드마크 인식기 초기화
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    face_img = cv2.imread(image_file)
    face_img_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

    # 얼굴 인식
    faces = detector(face_img_gray)
    
    # 안경 이미지 불러오기
    glasses_img = cv2.imread(glasses_path, cv2.IMREAD_UNCHANGED)
    
    for face in faces:
        landmarks = predictor(face_img, face)

        ## TODO
        # left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        # right_eye = (landmarks.part(45).x, landmarks.part(45).y)
        # print('@@왼쪽눈@@', left_eye) # (477, 251)
        # print('@@오른쪽눈@@', right_eye) # (639, 266)

        left_eye_x = int((landmarks.part(39).x + landmarks.part(36).x) // 2)
        left_eye_y = int((landmarks.part(39).y + landmarks.part(36).y) // 2)
        right_eye_x = int((landmarks.part(45).x + landmarks.part(42).x) // 2)
        right_eye_y = int((landmarks.part(45).y + landmarks.part(42).y) // 2)
        left_eye = (left_eye_x, left_eye_y)
        right_eye = (right_eye_x, right_eye_y)

        cv2.circle(face_img, left_eye, 3, (0, 0, 255), -1)
        cv2.circle(face_img, right_eye, 3, (0, 0, 255), -1)

        # 눈 사이 각도 계산
        angle = np.rad2deg(np.arctan2(right_eye[1]-left_eye[1], right_eye[0]-left_eye[0]))

        # ==========================
        # # 안경 이미지 회전
        # rotated_glasses = cv2.rotate(glasses_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # rotated_glasses = cv2.rotate(rotated_glasses, cv2.ROTATE_90_CLOCKWISE)
        # M = cv2.getRotationMatrix2D((glasses_img.shape[1] / 2, glasses_img.shape[0] / 2), -angle, 1)
        # rotated_glasses = cv2.warpAffine(rotated_glasses, M, (glasses_img.shape[1], glasses_img.shape[0]))

        # # 안경 이미지 사이즈 조정
        # eye_distance = np.sqrt((right_eye[1]-left_eye[1])**2 + (right_eye[0]-left_eye[0])**2)
        # # scale_factor = eye_distance / rotated_sunglasses.shape[1] * 1.25
        # scale_factor = eye_distance / rotated_glasses.shape[1] * 2.25
        # resized_glasses = cv2.resize(rotated_glasses, (0,0), fx=scale_factor, fy=scale_factor)

        # # 안경 이미지 위치 계산
        # center_x = int((left_eye[0] + right_eye[0]) / 2) - int(resized_glasses.shape[1] / 2)
        # center_y = int((left_eye[1] + right_eye[1]) / 2) - int(resized_glasses.shape[0] / 4) - int(resized_glasses.shape[0] / 8)

        # # 안경 이미지 합성
        # for i in range(resized_glasses.shape[0]):
        #     for j in range(resized_glasses.shape[1]):
        #         if resized_glasses[i, j, 3] > 0:
        #             face_img[center_y + i, center_x + j, :] = resized_glasses[i, j, :3]

        # ==========================

        # 안경 이미지 사이즈 조정
        eye_distance = np.sqrt((right_eye[1] - left_eye[1])**2 + (right_eye[0] - left_eye[0])**2)
        scale_factor = eye_distance / glasses_img.shape[1] * 2.25
        resized_glasses = cv2.resize(glasses_img, (0, 0), fx=scale_factor, fy=scale_factor)

        # 안경 이미지를 회전시킬 캔버스(도화지) 생성
        canvas_height = int(resized_glasses.shape[0] * 2)
        canvas_width = int(resized_glasses.shape[1] * 2)
        canvas = np.zeros((canvas_height, canvas_width, 4), dtype=np.uint8)

        # 안경 이미지를 캔버스 중앙에 위치시킴
        start_y = canvas_height // 2 - resized_glasses.shape[0] // 2
        start_x = canvas_width // 2 - resized_glasses.shape[1] // 2
        end_y = start_y + resized_glasses.shape[0]
        end_x = start_x + resized_glasses.shape[1]
        canvas[start_y:end_y, start_x:end_x] = resized_glasses

        # 안경 이미지 회전
        M = cv2.getRotationMatrix2D((canvas_width / 2, canvas_height / 2), -angle, 1)
        rotated_glasses = cv2.warpAffine(canvas, M, (canvas_width, canvas_height))

        # 안경 이미지 위치 계산
        center_x = int((left_eye[0] + right_eye[0]) / 2) - int(rotated_glasses.shape[1] / 2)
        center_y = int((left_eye[1] + right_eye[1]) / 2) - int(rotated_glasses.shape[0] / 4) - int(rotated_glasses.shape[0] / 4)

        # 안경 이미지 합성
        for i in range(rotated_glasses.shape[0]):
            for j in range(rotated_glasses.shape[1]):
                if rotated_glasses[i, j, 3] > 0:
                    face_img[center_y + i, center_x + j, :] = rotated_glasses[i, j, :3]


    # face_img_res = cv2.cvtColor(face_img, cv2.COLOR_GRAY2BGR)

    # TEST - 저장해보기
    # cv2.imwrite('test.jpg', face_img)

    # 이미지를 바이트로 변환
    _, encoded_img = cv2.imencode('.jpg', face_img)
    img_base64 = base64.b64encode(encoded_img).decode('utf-8')

    return img_base64


@api_view(['GET'])
def get_csrf_token(request):
    # 클라이언트에게 CSRF 토큰을 반환
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST'])
@csrf_exempt
def fitting_face(request, id):
    ### 1) 리액트에서 받아온 안경 이미지
    try:
        # image_file = request.FILES.get('image')
        image_file = request.FILES['image']
        # print('@@이미지@@', image_file) # blob
        # print('@@타입@@', type(image_file)) # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        # print('@@이미지이름@@', image_file.name) # blob
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)


    ### 2) 이미지 임시 저장 - 경로 만들어주기
    image_path = os.path.join(settings.STATIC_ROOT, image_file.name)
    # print('@@이미지임시경로@@', image_path)

    with open(image_path, 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)
    

    ### 3) 리액트에서 받아온 안경 데이터 이미지 경로 불러오기
    id -= 2
    product_img = 'res' + str(id) + '.png'
    glasses_path = os.path.join(settings.DEFAULT_DIR, output_path, product_img)
    # print('@@안경경로@@', glasses_path)



    ### 4) 이미지 위에 안경 이미지 붙여서 반환
    fitted_face = run_fitting(glasses_path, image_path) # 누끼딴 안경 이미지 경로, 얼굴 이미지 경로


    # response_data = {'result': 'success', 'message': '이미지 처리 완료'}
    # return JsonResponse(response_data)

    # return Response({'fitted_face': fitted_face})
    # return JsonResponse({'image' : image_file})
    # return HttpResponse(image_file, content_type='image/jpeg')
    
    ### 5) HttpResponse로 이미지 반환
    response = HttpResponse(fitted_face, content_type='image/jpeg')
    return response