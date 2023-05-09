from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse
import numpy as np
import cv2
from django.shortcuts import render
import os
import asyncio
import time

face_xml = 'backend/eyeglassy/face_detection/haarcascade_frontalface_default.xml'
eye_xml = 'backend/eyeglassy/face_detection/haarcascade_eye.xml'


def main(request):
    return render(request, "face_detection/main.html")

'''
async def camera_stream():
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        # frame 처리 코드 ...

        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        await asyncio.sleep(0)  # 대기

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        #return render(request, 'face_detection/camera_stream.html', {'frame': frame_bytes})
'''
async def camera_stream():
    capture = cv2.VideoCapture(0)

      
    while True:
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        ret, frame = capture.read()

        # convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale frame
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # iterate over all detected faces
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # detect eyes within each detected face
            eyes = eyeCascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                # get the center point of each eye
                eye_center = (int(x + ex + 0.5 * ew), int(y + ey + 0.5 * eh))

                # draw a circle around the center of each eye
                cv2.circle(frame, eye_center, radius=4,
                        color=(0, 0, 255), thickness=-1)

                # send eye center coordinates to the client using WebSocket or other means
                # ...
                print('Eye Center:', eye_center)

        # encode the frame to JPEG format
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        # wait for a short time before capturing the next frame
        await asyncio.sleep(0.03)

        # yield the JPEG frame as an HTTP multipart response
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


async def video_feed(request):
    print("실행중")
    return StreamingHttpResponse(
        camera_stream(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )


def eye_info(request):
    if request.method == "POST":
        print("넘김")
        left_eye = request.POST.get("left_eye")
        right_eye = request.POST.get("right_eye")
        print(left_eye, right_eye)
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
