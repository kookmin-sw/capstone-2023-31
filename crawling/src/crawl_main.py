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

with open('sample_products.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# 이미지 저장
# def save_image(image):
#     image_num = 0
#     try:
#         if not os.path.exists('../media/input'):
#             os.makedirs('../media/input')
#         urllib.request.urlretrieve(image, 'input'+str(image_num)+'.jpg')
#     except:
#         print('error:', image_num)
        
# 크롤링
img_num = 0

for page in range(1, 4):
    url = product_list_url + str(page)
    driver.get(url)
    time.sleep(0.5) # 1초 기다림

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
        url = base_url + url
        product_info.append(url)

        # image url
        image = product.select_one('div.pd-thumb-rect > a > img')['src']
        image = base_url + image
        product_info.append(image)
        
        try:
            # if not os.path.exists('../media/input'):
            #     os.makedirs('../media/input')
            img_name = 'img' + str(img_num) + '.jpg'
            urllib.request.urlretrieve(image, './media/input/'+img_name) # 다른 폴더 저장으로 변경 필요
        except:
            print('error:', idx)

        # 파일 저장
        # writer.writerow(product_info)
        with open('sample_products.csv', 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(product_info)

        img_num += 1

    print('page: ', page)

print('done!')