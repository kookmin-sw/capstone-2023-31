import cv2
import os


# 이미지 경로 설정
base_dir="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/data/dataset/crop_dataset/test"
dirlist=["heart","oblong","oval","round","square"]

# 사진에서 얼굴 인식을 위해 cascade classifier 로드
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
for diry in dirlist:
    dir_path=os.path.join(base_dir,diry)
    for file in os.listdir(dir_path):
        img_path = os.path.join(dir_path,file)
        # 이미지 읽기
        img = cv2.imread(img_path)

        faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)


        
        for (x, y, w, h) in faces:
            
            face = img[y:y+h, x:x+w]
            # 크롭된 이미지 저장
            cv2.imwrite(img_path,face)
    print(diry,"crop 완")
            