import os
import numpy as np
from PIL import Image
from tensorflow.keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


# 카테고리(얼굴형) 리스트
categories = ['heart', 'oblong', 'oval', 'round', 'square']

# VGG 모델 불러오기
base_model = VGG16(weights='imagenet', include_top=True)
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
base_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train_vector"
# 훈련 데이터 로드
train_data = {}
for category in categories:
    filename = os.path.join(base_path,f"{category}_train.npz")
    data = np.load(filename)
    features = data['features']
    labels = np.full((features.shape[0],), category)  # 라벨 생성
    train_data[category] = {'features': features, 'labels': labels}
    print(f"{category}_train.npz 로드 완료")

# 테스트 이미지 폴더 경로
test_folder = '/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/test'

# 테스트 이미지 로드 및 특징 추출
test_features = []
test_labels = []
for category in categories:
    category_folder = os.path.join(test_folder, category)
    image_files = os.listdir(category_folder)
    for image_file in image_files:
        if "DS" in image_file:
            continue
        image_path = os.path.join(category_folder, image_file)
        img = image.load_img(image_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature = model.predict(x)
        test_features.append(feature.flatten())
        test_labels.append(category)
        print(".", end="")
    print(category, "끝////")

# 테스트 데이터의 크기를 맞추기 위해 모든 벡터를 동일한 크기로 조정
max_length = max(len(features) for features in test_features)
test_features = [np.pad(features, (0, max_length - len(features)), mode='constant') for features in test_features]

test_features = np.array(test_features)
test_labels = np.array(test_labels)
print("테스트 데이터 준비 완료")

# K-Nearest Neighbors(KNN) 분류기 초기화
knn = KNeighborsClassifier(n_neighbors=3)

# 각 카테고리에 대해 KNN 모델 학습 및 테스트
predictions = []
for category in categories:
    print("=" * 15, category, "=" * 15)
    train_features = train_data[category]['features']
    train_labels = train_data[category]['labels']
    
    # KNN 모델 학습
    knn.fit(train_features, train_labels)
    print("KNN 모델 학습 완료")
    
    # 테스트 데이터 예측
    category_predictions = knn.predict(test_features)
    predictions.append(category_predictions)

# 최종 예측 결과 결합
predictions = np.array(predictions).T

# 각 테스트 샘플의 최종 예측 결과 확인
final_predictions = []
for i in range(predictions.shape[0]):
    unique_labels, label_counts = np.unique(predictions[i], return_counts=True)
    most_common_label = unique_labels[np.argmax(label_counts)]
    final_predictions.append(most_common_label)

# 정확도 계산
accuracy = accuracy_score(test_labels, final_predictions)
print("정확도:", accuracy)
