import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import load_model
import os
from sklearn.neighbors import KNeighborsClassifier
import joblib


def load_model_and_knn(static_path):
    model_path = os.path.join(static_path, "face_shape_model.h5")
    knn_path = os.path.join(static_path, "knn_classifier.pkl")

    # Load the face shape classification model
    model = load_model(model_path)

    # Load the KNN classifier
    knn = joblib.load(knn_path)

    return model, knn


def extract_face(image, static_path):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    face_cascade = cv2.CascadeClassifier(os.path.join(static_path,"haarcascade_frontalface_default.xml"))
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Extract the face region
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        face = image[y:y + h, x:x + w]
        return face
    else:
        return None


def extract_features(face_image, model):
    x = image.img_to_array(face_image)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    # Adjust the feature vector dimension to 4096
    return features.flatten()[:4096]


def predict_face_shape(static_path, image_file):
    # Load the saved model and knn classifier
    model, knn = load_model_and_knn(static_path)
    face_shapes = ['heart', 'oblong', 'oval', 'round', 'square']

    # Load the input image
    input_image = cv2.imread(image_file)

    # Extract the face region from the image
    face = extract_face(input_image, static_path)

    if face is not None:
        # Convert the face region to RGB
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        # Resize the face region to match the input size of the classifier
        resized_face = cv2.resize(rgb_face, (224, 224))

        # Extract features from the face region using the loaded model
        features = extract_features(resized_face, model)

        # Reshape features to match the input shape of the classifier
        features = features.reshape(1, -1)

        # Predict the face shape using the trained k-nearest neighbors classifier
        predicted_label = knn.predict(features)

        # Map the predicted label to the face shape name
        predicted_shape = face_shapes[int(predicted_label)]

        return predicted_shape
    else:
        return None


def run_modeling(static_path, image_file):
    predicted_shape = predict_face_shape(static_path, image_file)
    return predicted_shape
