import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os

face_types = ["heart", "oval", "round", "square", "oblong"]
features = []
labels = []
base_path = "/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train_vector"
for face_type in face_types:
    data = np.load('{}_train.npz'.format(face_type))['features']
    print('{}_train.npz'.format(face_type),"load 완료")
    features.extend(data)
    labels.extend([face_type]*len(data))

features = np.array(features)
labels = np.array(labels)
'''
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42)
'''
print(".")
model = svm.SVC(kernel='linear', probability=True)
print(".")
model.fit(X_train, y_train)
print("저장")
joblib.dump(model, 'face_shape_svm_model.pkl')
y_pred = model.predict(X_test)
print('Accuracy: ', accuracy_score(y_test, y_pred))
joblib.dump(model, 'face_shape_svm_model.pkl')
