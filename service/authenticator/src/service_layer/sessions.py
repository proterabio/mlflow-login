from flask import current_app

auth = current_app.http_auth


@auth.verify_password
def verify_password(email: str, password: str) -> bool:
    pass
