import cv2
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model, load_model
import os
from sklearn.neighbors import KNeighborsClassifier

model = load_model("face_shape_model.h5")


base_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train_vector"

# Load the trained vectors
heart_data = np.load(os.path.join(base_path,'heart_train.npz'))['features']
oblong_data = np.load(os.path.join(base_path,'oblong_train.npz'))['features']
oval_data = np.load(os.path.join(base_path,'oval_train.npz'))['features']
round_data = np.load(os.path.join(base_path,'round_train.npz'))['features']
square_data = np.load(os.path.join(base_path,'square_train.npz'))['features']

# Create labels
heart_labels = np.zeros(len(heart_data))
oblong_labels = np.ones(len(oblong_data))
oval_labels = np.full(len(oval_data), 2)
round_labels = np.full(len(round_data), 3)
square_labels = np.full(len(square_data), 4)

# Combine data and labels
data = np.concatenate((heart_data, oblong_data, oval_data, round_data, square_data), axis=0)
labels = np.concatenate((heart_labels, oblong_labels, oval_labels, round_labels, square_labels), axis=0)

# Train a k-nearest neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(data, labels)
# 카테고리(얼굴형) 리스트
face_shapes = ['heart', 'oblong', 'oval', 'round', 'square']

# Function to load an image
def load_image(image_path):
    image = cv2.imread(image_path)
    return image

# Function to extract face region from the image
def extract_face(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Extract the face region
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        face = image[y:y+h, x:x+w]
        return face
    else:
        return None


def extract_features(face_image):
    x = image.img_to_array(face_image)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features.flatten()[:4096]  # Adjust the feature vector dimension to 4096

# ...

# Predict the face shape for a new image
def predict_face_shape(image_path):
    # Load the input image
    input_image = load_image(image_path)

    # Extract the face region from the image
    face = extract_face(input_image)

    if face is not None:
        # Convert the face region to RGB
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        # Resize the face region to match the input size of the classifier
        resized_face = cv2.resize(rgb_face, (224, 224))

        # Extract features from the face region using VGG16 model or any other pre-trained model
        features = extract_features(resized_face)

        # Reshape features to match the input shape of the classifier
        features = features.reshape(1, -1)

        # Predict the face shape using the trained k-nearest neighbors classifier
        predicted_label = knn.predict(features)

        # Map the predicted label to the face shape name
        predicted_shape = face_shapes[int(predicted_label)]

        return predicted_shape
    else:
        return None


    


# Example usage
image_path = 'example.jpg'  # Replace with the path to your input image
predicted_shape = predict_face_shape(image_path)
print('Predicted face shape:', predicted_shape)
