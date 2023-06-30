from flask import current_app, request
from schema import SchemaError

from authenticator.src.adapters import repository
from authenticator.src.entrypoint import sessions
from authenticator.src.service_layer import users
from authenticator.src.service_layer.users import http_auth, token_auth, exceptions
from authenticator.src.service_layer.validators import users_schema


@sessions.route('/', methods=['GET'])
def ping():
    return {'message': 'ok'}, 200


@sessions.route('/auth', methods=['GET'])
@http_auth.login_required
def authentication():
    return {'user': http_auth.current_user()}, 200


@sessions.route('/users', methods=['POST'])
@token_auth.login_required
def add_user():
    try:
        request_payload = users_schema.validate(data=request.json)
    except SchemaError:
        return {'message': {'error': 'invalid input'}}, 422

    try:
        users.create_user(
            username=request_payload['username'],
            email=request_payload['email'],
            password=request_payload['password'],
            users_repo=repository.UsersRepository(
                resource=current_app.dynamo_resource
            )
        )
    except exceptions as error:
        return {'message': {'error': str(error)}}, error.http_code

    return {'message': 'ok'}, 201


@sessions.route('/users/<string:email>', methods=['DELETE'])
@token_auth.login_required
def remove_user(email):
    try:
        users.delete_user(
            email=email,
            users_repo=repository.UsersRepository(
                resource=current_app.dynamo_resource
            )
        )
    except exceptions as error:
        return {'message': {'error': str(error)}}, error.http_code

    return {'message': 'ok'}, 201
