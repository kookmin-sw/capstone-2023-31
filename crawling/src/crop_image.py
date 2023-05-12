from PIL import Image
import cv2, sys
from matplotlib import pyplot as plt
import numpy as np

# 실행 경로 /crawling

# SAMPLE_DIR = r'./face-detection/assets/images/sample1.jpg'
# TEMP_DIR = r'./face-detection/assets/images/temp1.jpg'
# RES_DIR = r'./face-detection/assets/images/result1.png'
INPUT_DIR = r'./image/input/'
TEMP_DIR = r'./image/temp/'
OUTPUT_DIR = r'./image/output/'


## 이미지 자르기
### 이미지 띄우기

for idx in range(0, 20):
    try:
        img = cv2.imread(INPUT_DIR + 'img' + str(idx) + '.jpg')
        img_gray = cv2.imread(INPUT_DIR + 'img' + str(idx) + '.jpg', cv2.IMREAD_GRAYSCALE)

        ### 가우시안 블러
        blur = cv2.GaussianBlur(img_gray, ksize=(3,3), sigmaX=0)
        ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

        edged = cv2.Canny(blur, 10, 250)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 컨투어 경계 찾기
        total = 0

        contours_xy = np.array(list(contours), dtype=object)

        ### x 최솟값 최댓값 찾기
        x_min, x_max = 0, 0
        tmp = list()
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                tmp.append(contours_xy[i][j][0][0])
                x_min = min(tmp)
                x_max = max(tmp)

        ### y 최솟값 최댓값 찾기
        y_min, y_max = 0, 0
        tmp = list()
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                tmp.append(contours_xy[i][j][0][1])
                y_min = min(tmp)
                y_max = max(tmp)

        ### image trim
        x = x_min
        y = y_min
        w = x_max - x_min
        h = y_max - y_min

        img_trim = img[y:y+h, x:x+w]
        cv2.imwrite(TEMP_DIR + 'temp' + str(idx) + '.jpg', img_trim)

        ##############
        ### 특정 픽셀의 rgb 구하기 -> white일 경우 투명 픽셀로 변경
        img = Image.open(TEMP_DIR + 'temp' + str(idx) + '.jpg')
        # img = cv2.imread(TEMP_DIR + 'temp' + str(idx) + '.jpg')
        img = img.convert('RGBA')
        datas = img.getdata()

        newData = []
        cutOff = 190

        for item in datas:
            if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)

        # 이미지 사이즈 조정 후 저장
        # print(img.size)
        img = img.resize((3064, 1164)) # 이미지 사이즈 조정
        img.save(OUTPUT_DIR + 'res' + str(idx) + '.png', 'PNG') # png로 저장
        # cv2.imwrite(OUTPUT_DIR + 'res' + str(idx) + '.png', img)
        # img_cropped = img.crop((0,0,300,300)) # 이미지 자르기

    except: # image idx 없는 경우
        continue # 해당 idx 패스