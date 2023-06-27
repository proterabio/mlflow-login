import boto3
import pytest


@pytest.fixture
def dynamodb_client():
    return boto3.resource(
        **{
            'service_name': 'dynamodb',
            'endpoint_url': 'http://dynamo:8000',
            'region_name': 'us-east-1',
        }
    )
