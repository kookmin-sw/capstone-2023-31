import Augmentor
import os

root_dir = os.path.join(os.getcwd(),"faceshape_master/published_dataset/train")


# loop over each class
dirlist=["heart","oblong","oval","round","square"]
for face_dir in dirlist:
	base_dir=os.path.join(root_dir,face_dir)
	for file in os.listdir(base_dir):
		# 이미지 증강할 데이터셋 경로 설정
		p = Augmentor.Pipeline(base_dir)

		# 다양한 증강 기법 적용
		p.rotate(probability=0.5, max_left_rotation=10, max_right_rotation=10)
		p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
		p.flip_left_right(probability=0.5)
		p.flip_top_bottom(probability=0.5)
		p.skew(probability=0.5, magnitude=0.3)
		p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)

		# 증강된 이미지 저장 폴더 경로 설정
		#save_dir=os.path.join(root_dir,"save/"+face_dir)
		p.sample(1000)    