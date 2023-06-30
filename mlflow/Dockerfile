FROM python:3.8.2-slim
LABEL authors="slopez"

WORKDIR /opt/mlflow

RUN pip install boto3 psycopg2-binary mlflow[extras]
COPY start_server.sh .

CMD ./start_server.sh