import cv2
import dlib
from PIL import Image, ImageDraw
import numpy as np
import os
from django.core.files.storage import default_storage

## media 폴더에 68.dat 추가해주기 !

def put_eyeglassy(static_path, image_file):
    # 얼굴 인식기와 랜드마크 인식기 초기화
    predictor_path = os.path.join(static_path, 'shape_predictor_68_face_landmarks.dat')

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    # 안경 이미지 불러오기
    # 리액트에서 받은 안경 정보 불러오기 TO DO
    # glass_img = Image.open('./face-detection/assets/images/result1.png')

    # TO DO
    ## 1. 리액트에서 얼굴 이미지, 씌울 안경 id 불러오기
    ## 2. 받은 안경 id 이용해서 /crawling/media/img/output 에 있는 해당 안경 이미지 파일 가져오기
    ## 3. 얼굴 이미지에 2번 이미지 씌우고 반환하기

    '''
    
    # 리액트에서 받은 이미지 읽어오기 TO DO

    # 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 인식
    faces = detector(gray)

    # 얼굴이 인식되었다면
    if len(faces) > 0:
        # 첫 번째 얼굴에 대해서 랜드마크 추출
        landmarks = predictor(gray, faces[0])

        # 왼쪽 눈과 오른쪽 눈의 중심 좌표 계산
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)
        eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)

        # 안경 이미지 크기 조정
        glass_width = right_eye[0] - left_eye[0]
        scale = glass_width / glass_img.width
        glass_height = int(scale * glass_img.height)
        glass_img_resized = glass_img.resize((glass_width, glass_height))

        # 안경 이미지를 회전시켜서 눈에 맞추기
        angle = -1 * (180 / 3.141592) * (left_eye[1] - right_eye[1]) / (left_eye[0] - right_eye[0])
        glass_img_rotated = glass_img_resized.rotate(angle, expand=True)

        # 안경 이미지를 프레임에 띄우기
        glass_left = eye_center[0] - glass_width // 2
        glass_top = eye_center[1] - glass_height // 2
        glass_right = glass_left + glass_img_rotated.width
        glass_bottom = glass_top + glass_img_rotated.height
        glass_region = (glass_left, glass_top, glass_right, glass_bottom)
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(frame_pil)
        draw.bitmap(glass_region[:2], glass_img)
        frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

    # 이미지 저장 후 리액트 전달 TO DO
    '''

def run_fitting(static_path, image_file):
    put_eyeglassy = put_eyeglassy(static_path, image_file)
    return put_eyeglassy
