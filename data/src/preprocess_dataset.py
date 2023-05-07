from PIL import Image
import numpy as np
import os
import time

def preprocess_image(image_path, target_size):
    # 이미지 불러오기
    image = Image.open(image_path)

    # 이미지 크기 조정
    image = image.resize(target_size)

    # 이미지 채널 수 조정
    image = image.convert('RGB')

    # 이미지 데이터 정규화
    image = np.array(image)
    image = image / 255.0

    return image

def preprocess_dataset(dataset_path, target_size):
    for foldername in os.listdir(dataset_path):
        if foldername not in dirlists:
            continue
        print(foldername)
        folderpath = os.path.join(dataset_path, foldername)
        label_images = []
        i = 0
        j = 0
        for filename in os.listdir(folderpath):
            if not filename.endswith('.jpg'):
                continue

            filepath = os.path.join(folderpath, filename)
            image = preprocess_image(filepath, target_size)
            label_images.append(image)
            i += 1
            
            if i % 3000 == 0:
                print(j,end=" ")
                # numpy 배열 형태로 변환
                label_images = np.array(label_images)
                print(label_images[0][0][0])
                # 레이블 별로 전처리된 이미지 저장 (이어쓰기 모드)
                np.savez(os.path.join(os.path.join(dataset_path,"data"), foldername + '_preprocessed_data_' + str(j) + '.npz'), images=label_images, label=foldername, append=j != 0)

                label_images = []  # 다음 배치를 위해 초기화
                j += 1
                time.sleep(5)
            
        if label_images:  # 마지막 배치 저장
            # numpy 배열 형태로 변환
            label_images = np.array(label_images)

            # 레이블 별로 전처리된 이미지 저장 (이어쓰기 모드)
            np.savez(os.path.join(os.path.join(dataset_path,"data"), foldername + '_preprocessed_data_' + str(j) + '.npz'), images=label_images, label=foldername, append=j != 0)
            print(j,end=" ")

#,"round"
dirlists=["heart","oval","square","oblong","round"]
dataset_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train/"

preprocess_dataset(dataset_path,(224, 224))
