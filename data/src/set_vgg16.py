from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
import numpy as np

# VGG16 모델 불러오기
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

# 얼굴형 클래스
face_types = ["heart", "oval", "round", "square", "oblong"]

# 각 얼굴형별 npz 파일들을 읽어 특징 벡터 추출
for face_type in face_types:
    combined_features = []
    
    for i in range(44):  # 파일 번호 범위에 맞게 수정
        filename = os.path.join(dataset_path, "data", "{}_preprocessed_data_{}.npz".format(face_type, i))
        data = np.load(filename)
        images = data['images']

        # 이미지 데이터를 전처리하여 VGG16 모델에 입력
        preprocessed_images = preprocess_input(images)
        features = model.predict(preprocessed_images)

        combined_features.extend(features)

    # 얼굴형별 특징 벡터 저장
    np.savez("{}_features.npz".format(face_type), features=combined_features)
