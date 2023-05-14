import csv
from pathlib import Path
import os

# csv_path = Path(__file__).resolve().parent.parent

with open('products_input.csv', mode='r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)

    # 새로운 열 추가
    headers.append('shape')

    # csv 파일 쓰기
    with open('products_output.csv', mode='w') as n_f:
        csv_writer = csv.writer(n_f)
        csv_writer.writerow(headers)  # 새로운 헤더 쓰기
        
    # 기존 내용과 새로운 열 추가해서 쓰기
    for row in csv_reader:
        row.append('round')
        csv_writer.writerow(row)