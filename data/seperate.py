import os
import shutil
import torch
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, random_split
import torchvision.transforms as transforms  # transforms import 추가


# 데이터셋 경로 설정
base_folder_path = "faceshape_master/published_dataset"
# 데이터셋 경로 설정

folder_name=["heart","oblong","oval","round","square"]
for folder in folder_name:
	#data_path=base_folder_path+folder
	#train_path=data_path+"/train"
	#test_path=data_path+"/test"
	data_path=base_folder_path+'/'+folder
	train_path=data_path+"/train"
	test_path=data_path+"/test"
	# train set 폴더 생성
	if not os.path.exists(train_path):
	    os.makedirs(train_path)

	for file in os.listdir(data_path):
		print(file)
	# test set 폴더 생성
	if not os.path.exists(test_path):
	    os.makedirs(test_path)

	# ImageFolder로 데이터셋 불러오기
	dataset = ImageFolder(root=data_path, transform=transforms.ToTensor())

	# 데이터셋 크기 설정
	dataset_size = len(dataset)

	# train set과 test set의 크기 비율 설정
	train_size = int(0.8 * dataset_size)
	test_size = dataset_size - train_size

	# train set과 test set으로 데이터셋 분리
	train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

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
