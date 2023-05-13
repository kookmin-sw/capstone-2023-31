import os
import numpy as np
from PIL import Image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model
from sklearn.neighbors import KNeighborsClassifier

base_path = "/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train_vector"

# 카테고리(얼굴형) 리스트
categories = ['heart', 'oblong', 'oval', 'round', 'square']
base_model = VGG16(weights='imagenet', include_top=False) # include_top을 False로 설정하여 마지막 레이어 포함하지 않음
x = base_model.output
x = Dense(4096, activation='relu')(x) # 추가적인 fully connected layer 추가
x = Dense(4096, activation='relu')(x) # 추가적인 fully connected layer 추가
predictions = Dense(len(categories), activation='softmax')(x) # 클래스 개수에 맞게 출력 레이어 수정

model = Model(inputs=base_model.input, outputs=predictions)
# 훈련 데이터 로드
train_data = {}
for category in categories:
    filename = f"{category}_train.npz"
    data = np.load(os.path.join(base_path, filename))
    features = data['features']
    labels = np.full((features.shape[0],), category) # 라벨 생성
    train_data[category] = {'features': features, 'labels': labels}
    print(f"{category}_train.npz 로드 완료")

# 훈련 데이터 준비
train_features = []
train_labels = []

for category, data in train_data.items():
    features = data['features']
    labels = data['labels']
    train_features.extend(features)
    train_labels.extend(labels)

# 배열로 변환
train_features = np.array(train_features)
train_labels = np.array(train_labels)

# 이미지 형태로 reshape
#train_features = train_features.reshape((-1, height, width, channels))

# 전처리
preprocessed_train_features = preprocess_input(train_features)

# 모델 훈련
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(preprocessed_train_features, train_labels, epochs=10, batch_size=32)
