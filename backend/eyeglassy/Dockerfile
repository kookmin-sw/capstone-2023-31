FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends libgl1-mesa-glx libglib2.0-0

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install tensorflow

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
