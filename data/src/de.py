import os
import numpy as np


base_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train/reduce_data/total"


face_types = ["heart", "oval", "round", "square", "oblong"]


# 각 얼굴형에 대한 데이터를 저장할 딕셔너리 초기화
merged_data = {shape: [] for shape in face_types}

# .npz 파일을 얼굴형에 따라 데이터를 저장
for shape in face_types:
    for i in range(1, 3):  # 1과 2의 인덱스를 가진 파일을 합침
        filename = os.path.join(base_path,f"{shape}_features{i}.npz")
        data = np.load(filename)
        features = data['features']
        merged_data[shape].append(features)

# 각 얼굴형에 대한 데이터를 합침
merged_data = {shape: np.concatenate(features_list, axis=0) for shape, features_list in merged_data.items()}

# 합쳐진 데이터를 저장
for shape, features in merged_data.items():
    output_filename = f"{shape}_merged.npz"
    np.savez(output_filename, features=features)
