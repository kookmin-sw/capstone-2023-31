from PIL import Image
import numpy as np
import os

def preprocess_image(image_path, target_size):
    # 이미지 불러오기
    image = Image.open(image_path)

    # 이미지 크기 조정
    image = image.resize(target_size)

    # 이미지 채널 수 조정
    image = image.convert('RGB')
    print(".",end="")
    # 이미지 데이터 정규화
    image = np.array(image)
    image = image / 255.0

    return image

def preprocess_dataset(dataset_path, target_size):
    images = []
    labels = []

    # 데이터셋 경로에서 이미지 파일을 불러와 전처리
    for foldername in os.listdir(dataset_path):
        if foldername not in dirlists: continue
        folderpath = os.path.join(dataset_path, foldername)
        for filename in os.listdir(folderpath):
            if not filename.endswith('.jpg'):
                continue
            
            filepath = os.path.join(folderpath, filename)
            image = preprocess_image(filepath, target_size)
            
            images.append(image)
            labels.append(foldername)
            

    # numpy 배열 형태로 변환
    images = np.array(images)
    labels = np.array(labels)

    return images, labels


dirlists=["heart","oblong","oval","round","square"]
dataset_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train/"

images, labels=preprocess_dataset(dataset_path,(224, 224))
np.savez('preprocessed_data.npz', images=images, labels=labels)
