from django.shortcuts import render
import requests
from django.conf import settings
import json
from bs4 import BeautifulSoup
from lxml import html
sample_b = "8801047284482"

#def crawl():


def test_main(request):
    return render(request, "main.html")


def search_product_by_barcode(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        response = requests.get(f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json')
        data = response.json()
        if data['status'] == 1:
            # 제품 정보가 있는 경우
            #product = data['product']['product_name']
            product = data['product']
            return render(request, 'result.html', {'product': product})
        else:
            # 제품 정보가 없는 경우
            message = '제품 정보를 찾을 수 없습니다.'
            return render(request, 'result.html', {'message': message})
    else:
        return render(request, 'search.html')

def search_nutrition_by_name(request): #식품안전나라에서 크롤링해서 성분 뽑아내기
    search_url = "http://www.foodsafetykorea.go.kr/portal/specialinfo/searchInfoProduct.do?menu_grp=MENU_NEW04&menu_no=2815"
    product_name = '보성홍차 아이스티'

    # 웹 페이지 가져오기
    response = requests.get(search_url)

    # HTML 파싱하기
    tree = html.fromstring(response.content)

    # 특정 경로에 위치한 텍스트 필드 찾기
    text_field = tree.xpath("//div[@class='main']/section/div[2]/div[1]/div[2]/div/dl/dd[3]")

    # 텍스트 필드에 입력할 값
    text_to_input = product_name

    # 텍스트 필드에 값 입력
    text_field.text = text_to_input
    print(html.tostring(tree, pretty_print=True))



def search_detail_by_name(request): #제품 정보 
    product_name ='보성홍차 아이스티'
    client_id = "Ijk_lTy1VGslskGRwYiH"
    client_secret = "dFNdCSrTuP"
    
    query = request.GET.get(product_name)  # 검색어
    print(query)
    # 네이버 검색 API URL
    url = 'https://openapi.naver.com/v1/search/shop.json'
    headers = {'X-Naver-Client-Id': client_id,
               'X-Naver-Client-Secret': client_secret}  # API 요청 헤더
    params = {
        'query': product_name,
        'display': 2
    }
    response = requests.get(url, headers=headers, params=params)


    search_result = response.json()  # 검색 결과(JSON) 파싱
    products = []
    for item in search_result['items']:
        item_info = {
            'title': item['title'],
            'image': item['image']
        }
        products.append(item_info)
        break

    return render(request, 'search_result.html', {'products': products})




