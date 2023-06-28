import os
from typing import Dict


def users_table() -> str:
    return os.getenv('USERS_TABLE_NAME')


def is_production() -> bool:
    return os.getenv('FLASK_ENV') == 'production'


def dynamodb_config() -> Dict:
    development_config = {
        'service_name': 'dynamodb',
        'endpoint_url': 'http://dynamo:8000',
        'region_name': 'us-east-1',
    }
    production_config = {
        'service_name': 'dynamodb',
        'region_name': 'us-east-1',
    }

    return production_config if is_production() else development_config
