import cv2
import dlib
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model

# Dlib 얼굴 감지기 및 특징 추출기 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#predictor=dlib.face_recognition_model_v1('models/dlib_face_recognition_resnet_model_v1.dat') 
# VGG 모델 로드
model = load_model("model.h5")

# 카테고리(얼굴형) 리스트
labels = ['heart', 'oblong', 'oval', 'round', 'square']


def preprocess_image(img):
    # 이미지 전처리
    img = cv2.resize(img, (224, 224))
    img = img.astype("float32")
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

def detect_face_landmarks(img):
    # 얼굴 감지 및 특징 추출
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    landmarks = []
    for face in faces:
        shape = predictor(gray, face)
        face_landmarks = [(shape.part(i).x, shape.part(i).y) for i in range(68)]
        landmarks.append(face_landmarks)

    return faces, landmarks



def predict_face_shape(img_path):
    # 얼굴 이미지 처리 및 얼굴 형상 예측
    img = cv2.imread(img_path)

    # 얼굴 감지 및 특징 추출
    faces, landmarks = detect_face_landmarks(img)
    # 얼굴 형상 예측
    predictions = []
    for face, landmark in zip(faces, landmarks):
        # 얼굴 영역 잘라내기
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        face_img = img[y:y+h, x:x+w]

        # 이미지 전처리 및 예측
        preprocessed_img = preprocess_image(face_img)
        predicted_classes = model.predict(preprocessed_img)
        print(np.argmax(predicted_classes))
        predicted_shape = labels[np.argmax(predicted_classes)]
        print(predicted_shape)

        # 예측 결과
        predictions.append(predicted_shape)

    return predictions

#사용자 얼굴 형상 예측


predicted_shapes = predict_face_shape("ex3.png")

#결과 출력
for predicted_shape in predicted_shapes:
    print("Predicted Face Shape:", predicted_shape)
    print("------------------------")
