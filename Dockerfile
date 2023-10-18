FROM python:3.11.0-slim

ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

COPY . .

RUN poetry install

EXPOSE 8000
