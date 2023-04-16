import numpy as np
import cv2
from django.shortcuts import render

font = cv2.FONT_ITALIC
face_xml = 'haarcascades/haarcascade_frontalface_default.xml'
eye_xml = 'haarcascades/haarcascade_eye.xml'
def main(request):
    return render(request,main.html)

def faceDetect(request):
    eye_detect = False
    face_cascade = cv2.CascadeClassifier(face_xml)
    eye_cascade = cv2.CascadeClassifier(eye_xml)

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
        cv2.putText(frame, info, (5, 15), font, 0.5, (255, 0, 255
