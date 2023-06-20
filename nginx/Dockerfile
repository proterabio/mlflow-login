FROM nginx:latest
LABEL authors="slopez"

RUN apt-get update -y && apt-get install apache2-utils -y

COPY nginx.conf /etc/nginx/nginx.conf