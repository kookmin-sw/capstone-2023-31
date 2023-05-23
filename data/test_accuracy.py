import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input

# 모델 로드
model = load_model('face_shape_model.h5')

# 테스트 이미지 폴더 경로
test_folder = './data/dataset/dataset/test' 

# 클래스 레이블
class_labels = ["heart", "oval", "round", "square", "oblong"]

# 테스트 이미지 폴더에서 이미지 로드 및 예측
predictions = []
true_labels = []

for label in class_labels:
    label_folder = os.path.join(test_folder, label)
    image_files = os.listdir(label_folder)
    
    for image_file in image_files:
        image_path = os.path.join(label_folder, image_file)
        
        # 이미지 로드 및 전처리
        try:
        	img = load_img(image_path, target_size=(224, 224))
        except: continue
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_preprocessed = preprocess_input(img_array)
        
        # 예측
        prediction = model.predict(img_preprocessed)
        predicted_label = np.argmax(prediction)
        
        predictions.append(predicted_label)
        true_labels.append(class_labels.index(label))

# 예측 결과 출력
for i in range(len(predictions)):
    print(f"Predicted: {class_labels[predictions[i]]}, True: {class_labels[true_labels[i]]}")

# 정확도 계산
accuracy = np.mean(np.array(predictions) == np.array(true_labels))
print(f"Test accuracy: {accuracy}")
