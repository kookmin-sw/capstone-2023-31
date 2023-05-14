import json
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Glasses

import os
from django.conf import settings


# csv_path = os.path.join(settings.DEFAULT_DIR, 'crawling/res_products.csv')

# csv 파일에서 데이터 읽어온 후 Glasses 모델에 저장
def load_glasses_data():
    with open('glasses.json', 'r') as f:
        glasses = json.load(f)
        new_list = []
        for glass in glasses:
            new_data = {'models': 'glasses.glass'}
            new_data['fields'] = glass
            new_list.append(new_data)

    with open('glasses_data.json', 'w', encoding='utf-8') as f:
        json.dump(new_list, f, ensure_ascii=False, indent=2)

    '''
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Glasses 객체 생성
            Glasses.objects.create(
                name = row['name'],
                price = row['cost'],
                brand = row['brand'],
                path = row['url'],
                image = row['image'],
                shape = row['shape']
            )
    return HttpResponse('Glasses data loaded successfully !')
    '''

load_glasses_data()