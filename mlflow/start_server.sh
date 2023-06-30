#!/bin/sh

mlflow server \
  --backend-store-uri postgresql://"${POSTGRES_USER}":"${POSTGRES_PASSWORD}"@"${POSTGRES_HOST}":5432/"${POSTGRES_DB}" \
  --default-artifact-root s3://"${AWS_BUCKET}"/artifacts \
  --host 0.0.0.0:5000 \
  --serve-artifacts
