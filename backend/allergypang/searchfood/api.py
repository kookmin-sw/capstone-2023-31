import requests
import xml.etree.ElementTree as ET

# API 요청 주소 생성
query = "8801047284482"
display = 10
start = 1
url = f"https://openapi.naver.com/v1/search/shop.xml?query={query}&display={display}&start={start}"

# API 요청
headers = {"X-Naver-Client-Id": "Ijk_lTy1VGslskGRwYiH",
           "X-Naver-Client-Secret": "dFNdCSrTuP"}
response = requests.get(url, headers=headers)

# API 응답 처리
root = ET.fromstring(response.text)
items = root.findall("./channel/item")
print(items)
for item in items:
    title = item.find("title").text
    link = item.find("link").text
    image = item.find("image").text
    print(title, link, image)
