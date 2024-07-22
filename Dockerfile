FROM python:3.12-slim

WORKDIR /usr/src/oarder

RUN apt update && \
    apt install -y curl make zip && \
    curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install

COPY . .
RUN poetry run make oarder.zip
COPY oarder.zip .
