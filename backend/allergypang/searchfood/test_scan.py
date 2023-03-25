import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detected = True
while detected:
    # 비디오에서 프레임 읽기
    ret, frame = cap.read()

    # 프레임에서 바코드 인식
    decodedObjects = pyzbar.decode(frame)
    
    # 바코드가 인식된 경우
    if len(decodedObjects) > 0:
        for obj in decodedObjects:
            # 바코드 텍스트 가져오기
            barcode_text = obj.data.decode("utf-8")
            print(barcode_text)
            detected=False
            
    # 프레임 표시
    cv2.imshow("Barcode Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 종료
cap.release()
cv2.destroyAllWindows()
'''
import xml.etree.ElementTree as ET
import requests
import pprint
import json
from django.conf import settings

#url = 'http://openapi.foodsafetykorea.go.kr/api/aee1cfc463594b10a12b/식품영양성분DB(NEW
# )/json/1/30'
url = 'http://openapi.foodsafetykorea.go.kr/api/aee1cfc463594b10a12b/C002/xml/1/3/BSSH_NM=오뚜기'
barcode_url = 'http://openapi.foodsafetykorea.go.kr/api/aee1cfc463594b10a12b/C005/xml/1/10/BSSH_NM=8801047284482'

response = requests.get(barcode_url)
contents = response.text

pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))
'''
