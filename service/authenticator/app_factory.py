import boto3
from flask import Flask, current_app

from authenticator.src import config
from authenticator.src.adapters import repository


def init_db(resource) -> None:
    try:
        repository.UsersRepository(resource).create_table()
    except repository.DynamoDBError:
        pass


def create_app():
    app = Flask(__name__)

    with app.app_context():
        current_app.dynamo_resource = boto3.resource(**config.dynamodb_config())

        from authenticator.src.entrypoint.views import sessions
        app.register_blueprint(sessions)

        init_db(current_app.dynamo_resource)
    return app


app_instance = create_app()
