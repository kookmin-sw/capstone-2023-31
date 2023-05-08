import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from PIL import Image
import cv2

def extract_sift_features(image_path):
    # 이미지를 그레이스케일로 로드합니다.
    image = cv2.imread(image_path, 0)

    # SIFT 객체를 생성합니다.
    sift = cv2.xfeatures2d.SIFT_create()

    # 이미지에서 특징점과 특징 벡터를 추출합니다.
    keypoints, descriptors = sift.detectAndCompute(image, None)

    return descriptors



# 카테고리(얼굴형) 리스트
categories = ['heart', 'oblong', 'oval', 'round', 'square']

# 이미지 폴더 경로
image_folder = '/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/test'

base_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train_vector"

# 특징 벡터 파일 로드
train_data = {}
for category in categories:
    filename = os.path.join(base_path,f"{category}_train.npz")
    data = np.load(filename)
    features = data['features']
    labels = np.full((features.shape[0],), category)  # 라벨 생성
    train_data[category] = {'features': features, 'labels': labels}
    print(category," 로드 완료")

# 이미지 로드 및 특징 추출
test_features = []
test_labels = []
for category in categories:
    category_folder = os.path.join(image_folder, category)
    image_files = os.listdir(category_folder)
    for image_file in image_files:
        if "DS" in image_file: continue
        image_path = os.path.join(category_folder, image_file)
        image = Image.open(image_path).convert('RGB')
        # 이미지를 특징 벡터로 변환하는 코드를 여기에 추가

        # SIFT 특징 벡터 추출
        feature = extract_sift_features(image_path)

        # 예시: feature = extract_features(image)
        test_features.append(feature)
        test_labels.append(category)
        print(".",end="")

    print(category,"끝////")
# 특징 벡터의 크기를 맞추기 위해 모든 벡터를 동일한 크기로 조정합니다.
max_length = max(len(features) for features in test_features)
test_features = [np.pad(features, ((0, max_length - len(features)), (0, 0)), mode='constant') for features in test_features ]

test_features = np.array(test_features)
test_labels = np.array(test_labels)
print("test numpy 생성완료")
# K-Nearest Neighbors(KNN) 분류기 초기화
knn = KNeighborsClassifier(n_neighbors=3)
print("knn 완료")


# 각 카테고리에 대해 KNN 모델 학습 및 테스트
predictions = []
for category in categories:
    print("="*15,category,"="*15)
    train_features = train_data[category]['features']
    train_labels = train_data[category]['labels']
    print("train data 로드완료")
    # KNN 모델 학습
    knn.fit(train_features, train_labels)
    print("knn 모델 학습완료")
    # 테스트 데이터 예측
    # 테스트 데이터 변환
    pca = PCA(n_components=4096)  # 원하는 차원 수로 설정
    # 학습 데이터 특징을 사용하여 PCA 모델을 학습합니다.
    flattened_train_features = np.vstack([train_data[category]['features'] for category in categories])
    pca.fit(flattened_train_features)
    # 테스트 데이터 변환
    flattened_test_features = np.vstack(test_features).reshape((-1, test_features[0].shape[1]))  # Reshape to 2D array

    # 학습된 PCA 모델을 사용하여 테스트 데이터 특징을 변환합니다.
    expanded_test_features = pca.transform(flattened_test_features)

    print("예측완료")
    predictions.append(category_predictions)

# 최종 예측 결과 결합
predictions = np.array(predictions).T
print("결과 결합 완료")
# 각 테스트 샘플의 최종 예측 결과 확인
final_predictions = []
for i in range(predictions.shape[0]):
    unique_labels, label_counts = np.unique(predictions[i], return_counts=True)
    most_common_label = unique_labels[np.argmax(label_counts)]
    final_predictions.append(most_common_label)

print("결과 확인 및 출력 준비 완료")
# 정확도 계산
accuracy = accuracy_score(test_labels, final_predictions)
print("Accuracy:", accuracy)
