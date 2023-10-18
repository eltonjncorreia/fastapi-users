FROM python:3.11.0-slim

ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

COPY . .

# Instale as dependências do Poetry
RUN poetry install

EXPOSE 8000

CMD [ "poetry", "run", "uvicorn", "--host", "0.0.0.0", "src.main:app" ]
