import Augmentor

## 증강 시킬 이미지 폴더 경로
img = Augmentor.Pipeline("D:/이미지 증강")

## 좌우 반전
img.flip_left_right(probability=1.0) 

## 상하 반전
img.flip_top_bottom(probability=1.0)

## 왜곡
img.random_distortion(probability=1, grid_width=10, grid_height=10, magnitude=8)

## 증강 이미지 수
img.sample(10)