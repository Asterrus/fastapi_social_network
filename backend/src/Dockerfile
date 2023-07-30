FROM python:3.11.1-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend/src

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
