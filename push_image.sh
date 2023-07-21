#!/usr/bin/env bash


if ! [ "$1" ]; then
  echo "error: you must the image name"
  exit 2
fi
repo_name=$1

if ! [ "$2" ]; then
  echo "error: you must provide the image type [dev, rc, latest]"
  exit 2
fi

if [ "$2" = "rc" ] || [ "$2" = "dev" ] || [ "$2" = "latest" ]; then
  image="$repo_name"":""$2"

  # get the account number associated with the current IAM credentials
  account=$(aws sts get-caller-identity --query Account --output text)

  if ! [ "$account" ]; then
    exit 255
  fi

  region=$(aws configure get region)
  region=${region:-us-east-1}

  fullname="${account}.dkr.ecr.${region}.amazonaws.com/${image}"

  # if the repository doesn't exist in ECR, create it.
  if ! aws ecr describe-repositories --repository-names "${repo_name}"; then
    aws ecr create-repository --repository-name "${repo_name}" >/dev/null
  fi

  # get the login command from ECR and execute it directly
  aws ecr get-login-password --region "${region}" | docker login --username AWS --password-stdin "${account}".dkr.ecr."${region}".amazonaws.com

  docker tag "${image}" "${fullname}"
  docker push "${fullname}"

else
  echo "error: you must provide the image type [dev, rc, latest]"
  exit 2
fi
