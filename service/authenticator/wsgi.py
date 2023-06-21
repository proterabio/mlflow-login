from flask import Flask, current_app
from flask_httpauth import HTTPBasicAuth


def create_app():
    app = Flask(__name__)

    with app.app_context():
        current_app.http_auth = HTTPBasicAuth()

    return app
