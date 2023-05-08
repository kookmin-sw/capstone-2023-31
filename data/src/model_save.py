import cv2
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
import os
from sklearn.neighbors import KNeighborsClassifier

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

# VGG16 모델 불러오기
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)

model.save("face_shape_model.h5")

print("Model saved successfully.")