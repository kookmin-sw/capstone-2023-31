#!/bin/sh

python csv_to_db.py
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000  --noreload

#gunicorn backend.wsgi:application --bin 0.0.0.0:8000