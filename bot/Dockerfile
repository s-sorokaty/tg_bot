FROM python:3.11-slim-buster

RUN apt update
RUN pip install poetry

COPY pyproject.toml poetry.lock /workspace/
RUN cd /workspace/ && poetry install
WORKDIR /workspace