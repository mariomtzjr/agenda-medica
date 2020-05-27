FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
COPY entrypoint.sh /code/entrypoint.sh

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN chmod +x /code/entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos el proyecto
COPY . /code/


# run entrypoin"t.sh
ENTRYPOINT ["sh", "/code/entrypoint.sh"]

