from flask import current_app, request

from authenticator.src.adapters import repository
from authenticator.src.entrypoint import sessions
from authenticator.src.service_layer import users
from authenticator.src.service_layer.users import http_auth


@sessions.route('/auth', methods=['GET'])
@http_auth.login_required
def authentication():
    return {'user': http_auth.current_user()}, 200


@sessions.route('/users', methods=['POST'])
def add_user():
    request_payload = request.json

    users.create_user(
        username=request_payload['username'],
        email=request_payload['email'],
        password=request_payload['password'],
        users_repo=repository.UsersRepository(
            resource=current_app.dynamo_resource
        )
    )
    return {'message': 'ok'}, 201
