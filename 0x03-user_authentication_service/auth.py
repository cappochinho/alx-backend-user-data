#!/usr/bin/env python3
"""Auth module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """This method takes a password string and
    returns a salted hash of the password
    using bcrypt.hashpw
    """

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf8'), salt)
