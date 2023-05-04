import os
import shutil
import torch
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, random_split
import torchvision.transforms as transforms  # transforms import 추가

# 데이터셋 경로 설정
base_folder_path = os.path.join(os.getcwd(),"faceshape_master/published_dataset")
print(base_folder_path)


folder_name=["heart","oblong","oval","round","square"]
#for folder in folder_name:
#data_path = os.path.join(base_folder_path, folder)
data_path=base_folder_path
train_path = os.path.join(data_path, "train")
test_path = os.path.join(data_path, "test")
'''
# 폴더 내의 모든 이미지 파일명을 JPEG 파일로 통일
for file in os.listdir(data_path):
	if file.startswith("img"):
		if file == ".jpg": 
			os.remove(file)
			print(file, ": 삭제")
			continue
		os.rename(os.path.join(data_path, file), os.path.join(data_path, file[:-4]+".jpg"))
'''
print(data_path)
# ImageFolder로 데이터셋 불러오기
dataset = ImageFolder(data_path, transform=transforms.Compose([transforms.ToTensor(),]))
# 데이터셋 크기 설정
dataset_size = len(dataset)

# train set과 test set의 크기 비율 설정
train_size = 80
test_size = 20

# train set과 test set으로 데이터셋 분리
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
# train set 폴더 생성
if not os.path.exists(train_path):
    os.makedirs(train_path)

# test set 폴더 생성
if not os.path.exists(test_path):
    os.makedirs(test_path)

# train set 이미지 저장
for i, (image, label) in enumerate(train_dataset):
    folder_name = dataset.classes[label]
    image_name = f'{i}.jpg'
    folder_path = os.path.join(train_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    image_path = os.path.join(folder_path, image_name)
    shutil.copy(image_path, image_path)

# test set 이미지 저장
for i, (image, label) in enumerate(test_dataset):
    folder_name = dataset.classes[label]
    image_name = f'{i}.jpg'
    folder_path = os.path.join(test_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    image_path = os.path.join(folder_path, image_name)
    shutil.copy(image_path, image_path)

# DataLoader로 데이터셋 불러오기
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
