from flask import current_app

from authenticator.src.adapters import repository
from authenticator.src.domain import model

auth = current_app.http_auth


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


@auth.verify_password
def authenticate_user(
        email: str,
        password: str,
        users_repo: repository.UsersRepository,
) -> str:
    user = users_repo.get_by_email(email=email)
    if not user:
        raise FailedAuth('wrong email or password')

    if not user.check_password(value=password):
        raise FailedAuth('wrong email or password')

    return user.username


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
    users_repo.delete(email=email)


def update_user(
        username: str,
        email: str,
        password: str,
        users_repo: repository.UsersRepository,
) -> None:
    user = users_repo.get_by_email(email=email)
    if not user:
        raise UserNotFound('user not found')

    user.email = email
    user.username = username
    user.password = password

    users_repo.update(user)
