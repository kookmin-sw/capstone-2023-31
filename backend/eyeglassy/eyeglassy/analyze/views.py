from django.shortcuts import render
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model
import joblib
import os
from django.conf import settings
import subprocess
from . import analyze

static_path = os.path.join(settings.BASE_DIR, 'media')


def run_modeling(image_file):
    # 외부 파이썬 파일 실행
    result = subprocess.run(
        ['python', 'analyze.py', static_path, image_file], capture_output=True, text=True)

    # 실행 결과 확인
    output = result.stdout
    error = result.stderr

    if result.returncode == 0:
        # 실행이 성공적으로 완료됨
        print("외부 파이썬 파일 실행 결과:", output)
        return output
    else:
        # 실행 중 오류가 발생함
        print("오류 발생:", error)

def main(request):
    return render(request, "analyze/main.html")


def upload(request):
    # 예상된 결과를 보여주는 뷰 함수
    return render(request, 'analyze/upload.html')


def show_result(request):
    if request.method == 'POST':
        # Get the uploaded image file from the form
        image_file = request.FILES['image']

        # Save the uploaded image file to the media directory
        image_path = os.path.join('media', image_file.name)
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        # Call the run_modeling function from analyze.py
        predicted_shape = analyze.run_modeling(static_path, image_path)

        if predicted_shape is not None:
            return render(request, 'analyze/result.html', {'predicted_shape': predicted_shape})
        else:
            return render(request, 'analyze/result.html', {'predicted_shape': 'No face detected'})

   
