from authenticator.src.domain import model


def test_validate_password():
    user = model.User(
        username='test',
        email='no-reply@test.com',
        password='SecurePassword'
    )

    assert user.check_password('SecurePassword')
    assert not user.check_password('SecurePassword1')
    assert user.password != 'SecurePassword'
    assert user._password != 'SecurePassword'
