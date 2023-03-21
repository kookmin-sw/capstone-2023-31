from django.shortcuts import render
import requests
from django.conf import settings
import json
sample_b = "8801047284482"


def test_main(request):
    return render(request, "main.html")


def search_product_by_barcode(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        response = requests.get(f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json')
        data = response.json()
        if data['status'] == 1:
            # 제품 정보가 있는 경우
            product = data['product']
            return render(request, 'result.html', {'product': product})
        else:
            # 제품 정보가 없는 경우
            message = '제품 정보를 찾을 수 없습니다.'
            return render(request, 'result.html', {'message': message})
    else:
        return render(request, 'search.html')



#def search_by_name(product):
