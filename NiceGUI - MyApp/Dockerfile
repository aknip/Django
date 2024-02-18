FROM python:3.8-slim

RUN apt update && apt install curl build-essential -y

WORKDIR /app

#COPY . .
COPY /app /app

RUN pip3 install -r requirements.txt

CMD python3 main.py
