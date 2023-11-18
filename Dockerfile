FROM python:3.12 AS base

ARG PROJECT_DIR=/project

ENV PYTHONUNBUFFERED 1

COPY . $PROJECT_DIR
WORKDIR $PROJECT_DIR

FROM base AS app

RUN pip install --upgrade pip pip-tools && \
    pip install -r $PROJECT_DIR/requirements.txt

FROM app AS dev-app

RUN pip install --upgrade pip pip-tools && \
    pip install -r $PROJECT_DIR/requirements-dev.txt

