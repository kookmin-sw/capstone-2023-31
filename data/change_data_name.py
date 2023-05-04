import os


# 데이터셋 경로 설정
base_folder_path = os.path.join(os.getcwd(),"faceshape_master/published_dataset")
print(base_folder_path)


folder_name=["heart","oblong","oval","round","square"]
for folder in folder_name:
	i=0
	data_path = os.path.join(base_folder_path, folder)

	for file in os.listdir(data_path):
		if file.startswith("img"):
			if file == ".jpg": 
				os.remove(file)
				print(file, ": 삭제")
				continue
			os.rename(os.path.join(data_path, file), os.path.join(data_path, str(i)+".jpg"))
			i+=1