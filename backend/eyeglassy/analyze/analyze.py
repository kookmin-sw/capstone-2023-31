import cv2
import numpy as np
import os
import boto3
import joblib


def load_model(static_path):
    model_path = os.path.join(static_path, 'face3.joblib')
    print(model_path)
    model = joblib.load(model_path)
    return model


def extract_face(image, static_path):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(os.path.join(
        static_path, "haarcascade_frontalface_default.xml"))
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        face = image[y:y + h, x:x + w]
        return face
    else:
        return None


def prepare_image(face_image):
    rgb_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
    resized_face = cv2.resize(rgb_face, (150, 150))
    normalized_image = resized_face / 255.0
    image_batch = np.expand_dims(normalized_image, axis=0)
    return image_batch


def predict_face_shape(static_path, image_file):
    model = load_model(static_path)
    face_shapes = ['Heart', 'Oblong', 'Square', 'Round', 'Oval']
    input_image = cv2.imread(image_file)
    face = extract_face(input_image, static_path)
    if face is not None:
        prepared_image = prepare_image(face)
        predicted_label = model.predict(prepared_image)
        predicted_index = np.argmax(predicted_label)
        predicted_shape = face_shapes[predicted_index]
        return predicted_shape
    else:
        return None


def run_modeling(static_path, image_file):
    predicted_shape = predict_face_shape(static_path, image_file)
    return predicted_shape
