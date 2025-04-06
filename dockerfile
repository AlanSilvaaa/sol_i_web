FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml .

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY ./src/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
