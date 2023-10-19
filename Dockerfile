FROM python:3.11.0-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN poetry install

EXPOSE 8000
