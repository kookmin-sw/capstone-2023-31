import cv2
import dlib
import numpy as np

# default dir : backend/eyeglassy
GLASSES_DIR = './fitting/images/glasses/glasses_sample.png'
FACE_DIR = './fitting/images/face/face_sample.jpg'
PREDICTOR_DIR = './fitting/shape_predictor_68_face_landmarks.dat'

# 이미지 로드
img = cv2.imread(FACE_DIR)
sunglasses = cv2.imread(GLASSES_DIR, cv2.IMREAD_UNCHANGED)

# detector, predictor 로드
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_DIR)

# 이미지 얼굴 인식
faces = detector(img)


for face in faces:
    # 랜드마크
    landmarks = predictor(img, face)

    # 랜드마크 찍기
    # for n in range(68):
    #     x = landmarks.part(n).x
    #     y = landmarks.part(n).y
    #     cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
    
    left_eye = (landmarks.part(40).x, landmarks.part(40).y)
    right_eye = (landmarks.part(46).x, landmarks.part(46).y)

    # cv2.circle(img, left_eye, 5, (0, 0, 255), -1)
    # cv2.circle(img, right_eye, 5, (0, 0, 255), -1)w

    # 눈 사이 각도 계산
    angle = np.rad2deg(np.arctan2(right_eye[1]-left_eye[1], right_eye[0]-left_eye[0]))

    # 안경 이미지 회전
    rotated_sunglasses = cv2.rotate(sunglasses, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rotated_sunglasses = cv2.rotate(rotated_sunglasses, cv2.ROTATE_90_CLOCKWISE)
    M = cv2.getRotationMatrix2D((sunglasses.shape[1] / 2, sunglasses.shape[0] / 2), -angle, 1)
    rotated_sunglasses = cv2.warpAffine(rotated_sunglasses, M, (sunglasses.shape[1], sunglasses.shape[0]))
    
    # rotated_sunglasses = cv2.rotate(sunglasses, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # rotated_sunglasses = cv2.rotate(rotated_sunglasses, cv2.ROTATE_90_CLOCKWISE)
    # sunglasses_height, sunglasses_width = rotated_sunglasses.shape[:2]
    # M = cv2.getRotationMatrix2D((sunglasses_width/2, sunglasses_height/2), angle, 1)
    # rotated_sunglasses = cv2.warpAffine(rotated_sunglasses, M, (sunglasses_width, sunglasses_height))

    # 안경 이미지 사이즈 조정
    eye_distance = np.sqrt((right_eye[1]-left_eye[1])**2 + (right_eye[0]-left_eye[0])**2)
    # scale_factor = eye_distance / rotated_sunglasses.shape[1] * 1.25
    scale_factor = eye_distance / rotated_sunglasses.shape[1] * 2
    resized_sunglasses = cv2.resize(rotated_sunglasses, (0,0), fx=scale_factor, fy=scale_factor)

    # 안경 이미지 위치 계산
    center_x = int((left_eye[0] + right_eye[0]) / 2) - int(left_eye[0] / 2)
    center_y = int((left_eye[1] + right_eye[1]) / 2) - int(resized_sunglasses.shape[0] / 2)

    # 안경 이미지 합성
    for i in range(resized_sunglasses.shape[0]):
        for j in range(resized_sunglasses.shape[1]):
            if resized_sunglasses[i,j,3] > 0:
                # img[center_y+i,center_x+j,:] = resized_sunglasses[i,j,:3]
                img[center_y+i,center_x+j,:] = resized_sunglasses[i,j,:3]

# 결과 이미지 출력
cv2.imshow('Output', img)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()

