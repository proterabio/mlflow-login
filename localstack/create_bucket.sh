#!/usr/bin/env bash

# prints a trace of simple commands
set -x
awslocal s3 mb s3://mlflow
# disables the trace
set +x
