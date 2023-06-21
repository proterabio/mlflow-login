from base64 import b64encode
from hashlib import sha256

from bcrypt import checkpw, hashpw, gensalt


class User:
    username: str
    password: str
    email: str

    def __init__(
            self,
            username: str,
            password: str,
            email: str,
    ):
        self.username = username
        self.password = password
        self.email = email

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = str(
            hashpw(
                b64encode(
                    sha256(value.encode('utf-8')).digest()
                ),
                gensalt()
            )
        ) if value else None

    def check_password(self, value: str) -> bool:
        return checkpw(
            b64encode(
                sha256(value.encode('utf-8')).digest()
            ),
            self._password.encode('utf-8')
        )
