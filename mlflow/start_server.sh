#!/bin/sh

mlflow server \
  --backend-store-uri postgresql://"${PG_USER}":"${PG_PWD}"@"${PG_HOST}":5432/"${PG_DB}" \
  --default-artifact-root s3://"${AWS_BUCKET}"/artifacts \
  --host 0.0.0.0:3000 \
  --serve-artifacts
