import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eyeglassy.settings")
django.setup()

from product.models import Glasses

with open('final_products.csv', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    next(rows, None) # 헤더 제외
    for row in rows:
        Glasses.objects.create(
            name = row[0],
            cost = row[1],
            brand = row[2],
            url = row[3],
            image = row[4],
            shape = row[5]
        )
        # print(row)
