import boto3
import pytest

from authenticator.app_factory import create_app


@pytest.fixture()
def flask_app():
    app = create_app()
    app.config.update(
        {
            'FLASK_ENV': 'testing',
        }
    )

    yield app


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()


@pytest.fixture
def dynamodb_client():
    return boto3.resource(
        **{
            'service_name': 'dynamodb',
            'endpoint_url': 'http://dynamo:8000',
            'region_name': 'us-east-1',
        }
    )
