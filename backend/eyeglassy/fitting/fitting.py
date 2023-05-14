import cv2
import dlib
from PIL import Image, ImageDraw
import numpy as np
import os
from django.core.files.storage import default_storage
from django.conf import settings

static_eyeglassy_path = os.path.join(settings.DEFAULT_DIR, 'crawling/img/')

## media 폴더에 68.dat 추가해주기 !


# 해당 안경 이미지 반환하는 함수
def specific_eyeglassy_img(eyeglassy_num):
    # eyeglassy_num은 3 같은 형식 일 것. (img3.jpg 에서 숫자 빼고 다 지워서)
    # 그럼으로 res3.png 에 해당하는 안경 누끼 이미지를 가져와야 함.
    res_path = 'output/res' + eyeglassy_num + '.png'
    eyeglassy_path = os.path.join(static_eyeglassy_path, res_path)
    print('eyeglassy_path : ', eyeglassy_path)
    
    return eyeglassy_path


# 안경 씌우고 이미지 반환하는 함수
def put_eyeglassy(static_path, image_file, eyeglassy_num):
    predictor_path = os.path.join(static_path, 'shape_predictor_68_face_landmarks.dat')

    # 얼굴 인식기와 랜드마크 인식기 초기화
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    # 얼굴 이미지 불러오기 (views.py에서 리액트에서 받아옴.)
    face_img = cv2.imread(image_file)
    face_gray_img = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY) # 그레이스케일로 변환

    # 얼굴 인식
    face = detector(face_gray_img)

    # 얼굴이 인식되었다면
    if len(face) > 0:
        # 랜드마크 추출
        landmarks = predictor(face_gray_img, face) # 이미지 1개에 대해서

        # 왼쪽 눈과 오른쪽 눈의 중심 좌표 걔산
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)
        eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)

        # 해당 안경 이미지 가져오기
        glass_img = specific_eyeglassy_img(eyeglassy_num) # res.png 경로가 되겠지

        # 안경 이미지 크기 조정
        glass_width = right_eye[0] - left_eye[0]
        scale = glass_width / glass_img.width
        glass_height = int(scale * glass_img.height)
        glass_img_resized = glass_img.resize((glass_width, glass_height))

        # 안경 이미지 크기 조정
        glass_width = right_eye[0] - left_eye[0]
        scale = glass_width / glass_img.width
        glass_height = int(scale * glass_img.height)
        glass_img_resized = glass_img.resize((glass_width, glass_height))

        # 안경 이미지를 회전시켜서 눈에 맞추기
        angle = -1 * (180 / 3.141592) * (left_eye[1] - right_eye[1]) / (left_eye[0] - right_eye[0])
        glass_img_rotated = glass_img_resized.rotate(angle, expand=True)

        # 안경 이미지를 씌우기 -> 가공된 이미지 반환
        glass_left = eye_center[0] - glass_width // 2
        glass_top = eye_center[1] - glass_height // 2
        glass_right = glass_left + glass_img_rotated.width
        glass_bottom = glass_top + glass_img_rotated.height
        glass_region = (glass_left, glass_top, glass_right, glass_bottom)
        face_pil = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
        draw = ImageDraw(face_pil)
        draw.bitmap(glass_region[:2], glass_img)
        face = cv2.cvtColor(np.array(face_pil), cv2.COLOR_RGB2BGR)

        # 이미지 저장 - 그냥 backend/ 안에?
        fitted_img = default_storage.save('fitted/' + image_file, face) # imgae.name -to do
        
        # 이미지 경로 반환
        return fitted_img


    # TO DO
    ## 1. 리액트에서 얼굴 이미지, 씌울 안경 id 불러오기
    ## 2. 받은 안경 id 이용해서 /crawling/media/img/output 에 있는 해당 안경 이미지 파일 가져오기
    ## 3. 얼굴 이미지에 2번 이미지 씌우고 반환하기


def run_fitting(static_path, image_file, eyeglassy_num):
    fitted_face = put_eyeglassy(static_path, image_file, eyeglassy_num) # 안경 쓴 이미지 경로
    return fitted_face
