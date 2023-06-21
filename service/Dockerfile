FROM python:3.8-buster
LABEL authors="slopez"

WORKDIR /opt/auth_server

COPY authenticator ./
RUN pip install -e .

ENTRYPOINT ["gunicorn", "-w","1","-b","0.0.0.0:5000","authenticator.src.wsgi:app"]