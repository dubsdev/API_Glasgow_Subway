FROM python:3.10.0b3-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT python api_gla_subway.py
