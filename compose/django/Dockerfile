FROM python:3.5.3-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update
RUN apk add --update \
    python-dev \
    build-base \
    linux-headers \
    pcre-dev \
    postgresql-dev
#    py-pip \
RUN pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi

RUN mkdir /code
WORKDIR /code
ADD requirements/base.txt /code/
ADD requirements/dev.txt /code/
RUN pip install -r base.txt -r dev.txt --retries 500 --timeout 600
ADD . /code/

WORKDIR /code