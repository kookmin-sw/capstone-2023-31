### 웹캠 동작 확인 샘플 코드 ###
### Sample code ###

import cv2
import dlib
from PIL import Image, ImageDraw
import numpy as np

# 얼굴 인식기와 랜드마크 인식기 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./face-detection/assets/models/shape_predictor_68_face_landmarks.dat') # 실행할 때 경로 주의

# 안경 이미지 불러오기
glass_img = Image.open('./face-detection/assets/images/result1.png')

# 웹캠 초기화
cap = cv2.VideoCapture(0)

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()

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

    # 이미지 출력
    cv2.imshow('frame', frame)

    # 종료하기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
