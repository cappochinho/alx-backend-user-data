#!/usr/bin/env python3
"""Auth module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """This method takes a password string and
    returns a salted hash of the password
    using bcrypt.hashpw
    """

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers a new user
        """

        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            passwd_hash = _hash_password(password)
            new_user = self._db.add_user(email, passwd_hash)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """authenticates user using email and password
        """

        try:
            user = self._db.find_user_by(email=email)
            match = bcrypt.checkpw(
                password.encode('utf8'),
                user.hashed_password
            )
            if match:
                return True
            else:
                return False
        except NoResultFound:
            return False
