from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import urllib
import os
import csv
from PIL import Image
# from urllib.request import urlopen


# 파일 실행 경로 : /crawling

regex = r'\([^)]*\)' # 괄호
regex2 = r'\[[^]]*\]' # 대괄호
base_url = 'https://www.top50glasses.com'
product_list_url = base_url + '/shop/goods/index.php?category=10&page='

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 엑셀
# filename = 'sample_crawlingdata.csv'
# f = open(filename, 'w', encoding='utf-8-sig', newline='')
# writer = csv.writer(f)
# title = 'sample_crawling_data'.split() # 엑셀 타이틀 제목
# writer.writerow(title)

header = ['name', 'cost', 'brand', 'url', 'image']

with open('./products.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# 이미지 저장
# def save_image(image):
#     image_num = 0
#     try:
#         if not os.path.exists('../image/input'):
#             os.makedirs('../image/input')
#         urllib.request.urlretrieve(image, 'input'+str(image_num)+'.jpg')
#     except:
#         print('error:', image_num)
        
# 크롤링
img_num = 0

for page in range(1, 69):
    url = product_list_url + str(page)
    driver.get(url)
    time.sleep(0.5) # 0.5초 기다림

    response = requests.get(product_list_url + str(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.select('#goods_list > div > div')

    # print('@@@ page @@@', page)
    for idx, product in enumerate(products):
        product_info = []
        # print('#', idx, '\n')
        
        # name
        try:
            name = product.select_one('p > a').text
            name = re.sub(regex, '', name)
            name = re.sub(regex2, '', name).strip()
        except:
            continue
        product_info.append(name)
        
        # cost
        try:
            cost = product.select_one('strong.text-price').text # 할인 들어가면 할인가 가져오기
            if '원' in cost:
                cost = cost.split('원')[0]
            cost = re.sub(',', '', cost).strip()
        except:
            cost = '없음'
        product_info.append(cost)

        # brand
        brand = product.select_one('small.text-gray-700').text
        product_info.append(brand)

        # url
        url = product.select_one('div.pd-thumb-rect > a')['href']
        url = re.sub('./store', '/store', url)
        url = base_url + '/shop/goods' + url
        product_info.append(url)

        # image url
        image_url = product.select_one('div.pd-thumb-rect > a > img')['src']
        image_url = base_url + image_url
        # product_info.append(image) # image url을 append 하지 말고, media 폴더에 저장하는 image이름을 append해주자.
        
        try:
            img_name = 'img' + str(img_num) + '.jpg'
            # print('***', img_name, os.getcwd())
            urllib.request.urlretrieve(image_url, './image/input/'+img_name)

            # 이미지 저장 다시 !!! 
            # img_name = 'img' + str(img_num) + '.jpg'
            # img = Image.open(image_url)
            # print(img)
            # img.save('./image/input/' + img_name, 'JPG')

            # img = Image.open(TEMP_DIR + 'temp' + str(idx) + '.jpg')
            # img = img.convert('RGBA')
            # img.save(OUTPUT_DIR + 'res' + str(idx) + '.png', 'PNG') # png로 저장
        except:
            print('error:', idx)
        product_info.append(img_name)

        # 파일 저장
        # writer.writerow(product_info)
        with open('./products.csv', 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(product_info)

        img_num += 1

    print('page: ', page)

print('done!')