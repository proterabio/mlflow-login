FROM python:3.8-buster
LABEL authors="slopez"

WORKDIR /opt/auth_server

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY authenticator ./

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]