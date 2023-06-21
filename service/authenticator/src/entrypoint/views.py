from authenticator.src.entrypoint import sessions
from flask import current_app

auth = current_app.http_auth


@sessions.route('/')
@auth.login_required
def index():
    return 'logged!'
