import cv2
import dlib
from PIL import Image, ImageDraw
import numpy as np
import os
from django.core.files.storage import default_storage
from django.conf import settings
import re

import os
import django

## fitting/models/ 폴더에 68.dat 추가해주기 !


# # 해당 안경 이미지 반환하는 함수
# def specific_eyeglassy_img(eyeglassy_num):
#     # eyeglassy_num은 3 같은 형식 일 것. (img3.jpg 에서 숫자 빼고 다 지워서)
#     # 그럼으로 res3.png 에 해당하는 안경 누끼 이미지를 가져와야 함.
#     res_path = 'output/res' + eyeglassy_num + '.png'
#     eyeglassy_path = os.path.join(static_eyeglassy_path, res_path)
#     print('eyeglassy_path : ', eyeglassy_path)
    
#     return eyeglassy_path



def run_fitting(glasses_path, image_file):

    # predictor_path = os.path.join(static_path, 'shape_predictor_68_face_landmarks.dat')
    predictor_path = 'models/shape_predictor_68_face_landmarks.dat'

    # 얼굴 인식기와 랜드마크 인식기 초기화
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    # 얼굴 이미지 불러오기 (views.py에서 리액트에서 받아옴.)
    face_img = cv2.imread(image_file)

    # 얼굴 인식
    faces = detector(face_img)
    
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
        
    # # show
    # cv2.imshow('output', face_img)
    # while True:
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord("q"):
    #         break
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 이미지 반환
    return face_img

