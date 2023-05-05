import os
from PIL import Image

base_dir="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/dataset/train/oblong"
for file in os.listdir(base_dir):
	if file==".DS_Store": continue
	# 이미지 파일 열기
	with Image.open(os.path.join(base_dir,file)) as im:
		if im.mode == 'P':
			im = im.convert('RGB')
			
		filename = os.path.splitext(file)[0]
		im.save(os.path.join(base_dir,filename+".jpg"), "JPEG")
