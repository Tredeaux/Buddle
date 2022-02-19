FROM python:3.8-alpine

RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libffi-dev \
    libpq

RUN mkdir /buddle_core
WORKDIR /buddle_core

COPY . .

RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1




