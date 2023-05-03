# 데이터 셋을 training set 과 test set으로 분류

import os
import numpy as np
from sklearn.model_selection import StratifiedKFold

# 이미지가 저장된 폴더 경로 설정
base_folder_path = '/Users/gimsubin/Desktop/2023/2023-1/real_capstone/face_deeplearning/faceshape-master/published_dataset/'
folder_name=["hear",'oblong','oval','round','square']
for folder in folder_name:
    # 이미지 파일 이름과 라벨을 저장할 리스트 생성
    filenames = []
    labels = []
    folder_path=base_folder_path+folder_name
    # 폴더 안에 있는 이미지 파일 이름과 라벨을 리스트에 저장
    for class_name in os.listdir(folder_path):
        class_path = os.path.join(folder_path, class_name)
        for filename in os.listdir(class_path):
            file_path = os.path.join(class_path, filename)
            filenames.append(file_path)
            labels.append(class_name)

    # 리스트를 numpy 배열로 변환
    filenames = np.array(filenames)
    labels = np.array(labels)

    # StratifiedKFold 객체 생성
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    # Training set과 Test set의 인덱스를 저장할 리스트 생성
    train_indexes_list = []
    test_indexes_list = []

    # K-fold cross-validation을 통해 Training set과 Test set의 인덱스를 구함
    for train_indexes, test_indexes in skf.split(filenames, labels):
        train_indexes_list.append(train_indexes)
        test_indexes_list.append(test_indexes)

    # 각 Fold별로 Training set과 Test set을 출력하여 확인
    for i, (train_indexes, test_indexes) in enumerate(zip(train_indexes_list, test_indexes_list)):
        print(f"Fold-{i}")
        print(f"Train set: {filenames[train_indexes]}")
        print(f"Test set: {filenames[test_indexes]}")
