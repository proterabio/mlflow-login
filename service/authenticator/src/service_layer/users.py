from typing import Optional

from flask import current_app
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from authenticator.src import config
from authenticator.src.adapters import repository
from authenticator.src.domain import model

http_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')


class UserNotFound(Exception):
    def __init__(self, message: str):
        self.http_code = 404
        super().__init__(message)


class FailedAuth(Exception):
    def __init__(self, message: str):
        self.http_code = 503
        super().__init__(message)


class DuplicatedEmail(Exception):
    def __init__(self, message: str):
        self.http_code = 422
        super().__init__(message)


exceptions = (
    UserNotFound,
    DuplicatedEmail
)


@http_auth.verify_password
def verify_password(
        username: str,
        password: str,
) -> Optional[str]:
    users_repo = repository.UsersRepository(
        resource=current_app.dynamo_resource
    )

    if not username or not password:
        return None

    user = users_repo.get_by_email(email=username)
    if not user:
        return None

    if not user.check_password(value=password):
        return None

    return user.username


@token_auth.verify_token
def verify_token(token: str) -> Optional[str]:
    return token if token == config.get_master_token() else None


def create_user(
        username: str,
        email: str,
        password: str,
        users_repo: repository.UsersRepository,
) -> None:
    user = users_repo.get_by_email(email=email)
    if user:
        raise DuplicatedEmail(f'the email {email} is already taken')

    new_user = model.User(
        username=username,
        email=email,
        password=password
    )
    users_repo.add(new_user)


def delete_user(
        email: str,
        users_repo: repository.UsersRepository,
) -> None:
    user = users_repo.get_by_email(email=email)
    if not user:
        raise UserNotFound(f'the user <{email}> does not exist')

    users_repo.delete(email=email)


def update_user(
        username: str,
        email: str,
        password: str,
        users_repo: repository.UsersRepository,
) -> None:
    user = users_repo.get_by_email(email=email)
    if not user:
        raise UserNotFound(f'the user <{email}> does not exist')

    user.email = email
    user.username = username
    user.password = password

    users_repo.update(user)
