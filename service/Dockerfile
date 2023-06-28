FROM python:3.8-buster
LABEL authors="slopez"

WORKDIR /opt/

RUN pip install --upgrade pip

COPY authenticator ./authenticator
COPY tests ./tests
COPY pyproject.toml .
RUN pip install -e .

ENTRYPOINT ["gunicorn", "-w","1","-b", "0.0.0.0:5000", "--reload" ,"authenticator.app_factory:app_instance"]