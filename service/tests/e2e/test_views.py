import base64

from authenticator.src import config


def test_create_user(client):
    with client:
        token = config.get_master_token()
        response = client.post(
            '/users',
            json={
                'username': 'flask',
                'email': 'flask@email.com',
                'password': 'SecurePassword'
            },
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 201
        assert response.json == {'message': 'ok'}


def test_login(client):
    email = 'flask@email.com'
    password = 'SecurePassword'

    valid_credentials = base64.b64encode(bytes(f'{email}:{password}', 'utf-8')).decode('utf-8')
    with client:
        response = client.get('/auth', headers={'Authorization': f'Basic {valid_credentials}'})
        assert response.status_code == 200


def test_duplicated_user(client):
    with client:
        token = config.get_master_token()
        response = client.post(
            '/users',
            json={
                'username': 'flask 2',
                'email': 'flask@email.com',
                'password': 'SecurePassword2'
            },
            headers={'Authorization': f'Bearer {token}'}
        )
        assert response.status_code == 409
        assert response.json == {'message': {'error': 'the email flask@email.com is already taken'}}
