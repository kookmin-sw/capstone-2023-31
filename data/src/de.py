
import os

import shutil


dirlists=["oval","square","round","oblong"]
base_dir="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train"
for dirlist in dirlists:
    target_folder=os.path.join(base_dir,dirlist)
    print(dirlist)

    dataset_path=os.path.join(target_folder,"output")
    for file in os.listdir(dataset_path):
        if file==".DS_Store": continue
        image_path=os.path.join(dataset_path,file)
        # 대상 폴더가 존재하지 않으면 생성
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # 이미지 파일을 대상 폴더로 이동
        shutil.move(image_path, target_folder)
        print(".",end="")

