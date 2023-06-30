from authenticator.src import config
from authenticator.src.adapters import repository
from authenticator.src.domain import model


def test_write_user(dynamodb_client):
    user = model.User(
        username='test',
        email='no-reply@test.com',
        password='SecurePassword'
    )

    users_repo = repository.UsersRepository(dynamodb_client)
    users_repo.add(item=user)

    table = dynamodb_client.Table(config.users_table())
    response = table.get_item(Key={'email': user.email})

    assert response['Item']['username'] == user.username


def test_result_type(dynamodb_client):
    user = model.User(
        username='test',
        email='no-reply@test.com',
        password='SecurePassword'
    )

    users_repo = repository.UsersRepository(dynamodb_client)
    users_repo.add(item=user)

    # noinspection PyTypeChecker
    assert isinstance(
        users_repo.get_by_email(email=user.email),
        model.User
    )


def test_delete_user(dynamodb_client):
    user = model.User(
        username='test',
        email='no-reply@test.com',
        password='SecurePassword'
    )

    users_repo = repository.UsersRepository(dynamodb_client)
    users_repo.add(item=user)
    users_repo.delete(email=user.email)

    assert not users_repo.get_by_email(email=user.email)
