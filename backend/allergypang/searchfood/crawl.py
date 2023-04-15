from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pymysql
import time
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

# 검색할 단어 설정
product_name = '보성홍차 아이스티'

#//*[@id="tbody"]
# 검색창 URL 설정
url = "http://www.foodsafetykorea.go.kr/portal/specialinfo/searchInfoProduct.do?menu_grp=MENU_NEW04&menu_no=2815"

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

driver.get(url)
# 텍스트 입력
input_element = driver.find_element("id","prd_nm")
input_element.clear()  # 텍스트 입력 전에 먼저 입력 칸을 비웁니다.
input_element.send_keys(product_name)
driver.find_element("xpath",'//*[@id="srchBtn"]').click()
time.sleep(3)

wait = WebDriverWait(driver, 10)

print("검색 중")
# 기다리고자 하는 요소와 값 설정
#root=//*[@id = "div_totCnt"]/text()[1] 총 건수 조회중...
element_locator = (By.ID, "tbl_prd_list")
expected_value = "조회된 데이터가 없습니다."
# //*[@id="div_totCnt"]/strong

# WebDriverWait 객체 생성 후 until() 함수 사용
wait = WebDriverWait(driver, 50)  # 최대 10초까지 대기

wait.until_not(EC.text_to_be_present_in_element(element_locator, expected_value))
print("검색완료")
time.sleep(7)
wait = WebDriverWait(driver, 30)
table = wait.until(EC.presence_of_element_located(By.XPATH,'//*[@id="div_totCnt"]/strong'))
a = driver.find_element("xpath", '//*[@id="div_totCnt"]/strong')
if a.text == 0:
    print("조회 불가능")

wait = WebDriverWait(driver, 30)
table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
tr_tags = table.find_elements(By.TAG_NAME, "tr")
print("로딩 끝")
# tbody 태그 안에 있는 모든 tr 태그 찾기
#tr_tags = driver.find_element(By.ID,"tbody").find_elements(By.TAG_NAME, 'tr')

# 마지막 tr 태그 선택하기
last_tr_tag = tr_tags[-1]
last_tr_tag.find_element(By.TAG_NAME,'a').click()
#wait = WebDriverWait(driver, 30)
#wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
print("상세페이지 접속")
#time.sleep(10)
# 검색 결과 크롤링
d1 = driver.find_element(By.CLASS_NAME, "fancybox-skin")
d2=d1.find_element(By.TAG_NAME, 'tbody')
d3=d2.find_elements(By.TAG_NAME, 'tr')
#html = driver.page_source
#soup = BeautifulSoup(html, "html.parser")

#results = soup.find_all("tbody")


# 결과 출력
for result in results:
    detail=result.find_elements(By.TAG_NAME,'td')
    nutrition=detail[1].text
    print(nutrition)
time.sleep(15)
# 브라우저 닫기
driver.quit()
