from base64 import b64encode
from hashlib import sha256
from typing import Optional

from bcrypt import checkpw, hashpw, gensalt


class User:
    username: str
    password: str
    email: str

    def __init__(
            self,
            username: str,
            email: str,
            password: Optional[str] = None,
    ):
        self.username = username
        if password:
            self.password = password
        else:
            self._password = None
        self.email = email

    def __iter__(self):
        allowed_attrs = {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }
        for key, value in allowed_attrs.items():
            yield key, value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = hashpw(
            b64encode(
                sha256(value.encode('utf-8')).digest()
            ),
            gensalt()
        ).decode('utf-8') if value else None

    def check_password(self, value: str) -> bool:
        return checkpw(
            b64encode(
                sha256(value.encode('utf-8')).digest()
            ),
            self._password.encode('utf-8')
        )
