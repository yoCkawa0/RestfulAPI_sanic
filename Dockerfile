# FROM python:3.8.5-slim-buster
FROM python:3.8
# docker pull python:3.8.5-slim-buster

# ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api

ENV POETRY_VERSION=1.1.5 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

ENV PATH="$POETRY_HOME/bin:$PATH"


# 依存関係のコピー
COPY ./pyproject.toml ./api
COPY . /api
# poetryのインストール
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV POETRY_NO_INTERACTION=1
# RUN pip install --upgrade pip
RUN poetry new api_sanic
RUN poetry shell
# 依存関係のインストール
RUN poetry install
# RUN pip install -r requirements.txt
# COPY . /api
# EXPOSE 5432
EXPOSE 8000
# CMD [ "python3", "./api_sanic/main.py" ]