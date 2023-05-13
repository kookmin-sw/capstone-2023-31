import numpy as np
import os

data_list = []
label_list = []
dirlists=["heart","oblong","oval","round","square"]
dataset_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train/"
default_path="_preprocessed_data.npz"

for dirs in dirlists:
    filename=os.path.join(dataset_path,dirs+default_path)
    print(filename)
    data = np.load(filename)['images']
    label = np.load(filename)['label']
    data_list.append(data)
    label_list.append(label)

# 리스트를 numpy 배열로 변환
data_array = np.concatenate(data_list, axis=0)
label_array = np.concatenate(label_list, axis=0)

# VGG 모델 입력에 맞게 이미지 데이터 shape 조정
data_array = np.repeat(data_array[..., np.newaxis], 3, -1)

# 전처리된 이미지 데이터와 레이블을 저장할 npz 파일 생성
np.savez('merge_preprocessed_data.npz', images=data_array, labels=label_array)



