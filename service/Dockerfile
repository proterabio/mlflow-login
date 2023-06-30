FROM python:3.8-buster
LABEL authors="slopez"

WORKDIR /opt/

RUN pip install --upgrade pip

COPY pyproject.toml .
COPY authenticator ./authenticator
RUN pip install -e .
COPY tests ./tests
COPY start_server.sh .

ENTRYPOINT ./start_server.sh