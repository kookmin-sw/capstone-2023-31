import numpy as np
import cv2
from django.shortcuts import render
import os


#face_xml = 'haarcascades/haarcascade_frontalface_default.xml'
#eye_xml = 'haarcascades/haarcascade_eye.xml'
def main(request):
    return render(request,"main.html")

def faceDetect(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    face_xml = os.path.join(\
    BASE_DIR, 'face_detection/haarcascades/haarcascade_frontalface_default.xml')
    eye_xml = os.path.join(\
    BASE_DIR, 'face_detection/haarcascades/haarcascade_eye.xml')

    font = cv2.FONT_ITALIC

    eye_detect = False
    face_cascade = cv2.CascadeClassifier(face_xml)
    eye_cascade = cv2.CascadeClassifier(eye_xml)
    if face_cascade.empty():
        print("Error loading face cascade file")


    if eye_cascade.empty():
        print("Error loading eye cascade file")

    try:
        capture = cv2.VideoCapture(0)  # 노트북 웹캠 카메라
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    except:
        print('camera loading error')
        return render(request, 'error.html')

    while(True):
        ret, frame = capture.read()
        if not ret:
            break

        if eye_detect:
            info = 'Eye Detection ON'
        else:
            info = 'Eye Detection OFF'

        frame = cv2.flip(frame, 1)  # 좌우대칭
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 1.05, 5 ?
        print('Numbers of faces detected: ' + str(len(faces)))

        # 카메라 영상 왼쪽 위에 셋팅된 info의 내용 출력
        cv2.putText(frame, info, (5, 15), font, 0.5, (255, 0, 255), 1)

        if len(faces):
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (int(x), int(y)), (int(x+w),
                              int(y+h)), (255, 0, 0), 2)  # 사각형 범위
                cv2.putText(frame, 'Detected Face', (x-5, y-5),
                            font, 0.5, (255, 255, 0), 2)  # 얼굴 찾았다는 메세지
                if eye_detect:  # 눈 찾기
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey),
                                      (ex+ew, ey+eh), (0, 255, 0), 2)

            # 이미지 프레임을 byte 형식으로 변환
            _, jpeg = cv2.imencode('.jpg', frame)
            data = []
            data.append(jpeg.tobytes())

            return render(request, 'face_detection.html', {'data': data})

            








