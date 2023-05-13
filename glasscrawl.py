from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import os
import time
import csv
'''
# DB 접속 정보 설정
host = 'localhost'
user = 'root'
password = 'mypassword'
database = 'mydatabase'

# DB 연결
db = pymysql.connect(host=host, user=user, password=password,
                     db=database, charset='utf8mb4')
'''
# 필요한 라이브러리 import
glass_info={}
media_path="/Users/gimsubin/Desktop/2023/2023-1/real_capstone/capstone-2023-31/backend/eyeglassy/media/glass_img"
#//*[@id="tbody"]
# 검색창 URL 설정
url = "https://www.top50glasses.com/shop/goods/index.php?category=10&page="

# 크롬 브라우저 옵션 설정
options = Options()

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# ChromeDriver 경로 설정
chrome_driver_path = "/Users/gimsubin/Downloads/chromedriver"
chrome_service = webdriver.chrome.service.Service(
    executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 텍스트 입력
i=30
for page in range(4,16):
	page_url=url+str(page)
	#print(page_url)
	driver.get(page_url)
	#product_lists=driver.find_element(By.XPATH,'//*[@id="goods_list"]/div')
	#product_list=[//*[@id="goods_list"]/div/div
	#print(product_list)
	for idx in range(1,10):
		product='//*[@id="goods_list"]/div/div['+str(idx)+']'
		link=driver.find_element(By.XPATH,product+'/div/div[1]/div[2]/a')
		product_url=link.get_attribute("href")
		link=driver.find_element(By.XPATH,product+'/div/div[2]/p/a')
		product_name=link.text
		try: 
			product_price=driver.find_element(By.XPATH,product+'/div/div[2]/div[1]/strong[2]').text
		except:
			product_price=driver.find_element(By.XPATH,product+'/div/div[2]/div[1]/strong').text

		# XPath 표현식으로 이미지 가져오기
		img = driver.find_element(By.XPATH,product+'/div/div[1]/div[2]/a/img')

		# 이미지 URL 가져오기
		img_url = img.get_attribute("src")

		# 이미지 다운로드
		img_data = requests.get(img_url).content

		# 이미지 이름 변환
		img_name = "img"+str(i)+".jpg"

		

		# 이미지 저장 경로 설정
		img_path = os.path.join(media_path, img_name)

		# 이미지 파일 저장
		with open(img_path, "wb") as handler:
		    handler.write(img_data)
		glass_info[i]=[i,product_name,product_price,product_url]    #이름, 가격, 링크 순으로 
		# 결과 출력
		print("이미지가 성공적으로 저장되었습니다.")

		i+=1

		
		if i==2:
			print(img_path)
			print(glass_info)




# CSV 파일 이름 설정
filename = "product_info.csv"

# CSV 파일에 저장할 헤더 정보 설정
header = ["Product Id","Product Name", "Product Price", "Product URL"]

# CSV 파일 열기
with open(filename, "w", encoding="utf-8", newline="") as csvfile:
    
	# CSV writer 생성
	writer = csv.writer(csvfile)

	# 헤더 정보 쓰기
	writer.writerow(header)
	for j in range(1,i-29):
		writer.writerow(glass_info[j+29])

# 결과 출력
print("CSV 파일에 제품 정보가 저장되었습니다.")
csvfile.close()
# 브라우저 닫기
driver.quit()