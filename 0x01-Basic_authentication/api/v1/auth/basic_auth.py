#!/usr/bin/env python3
"""
Contains the class BasicAuth, that inherits from Auth
"""

import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Class for Basic Authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract a Base64 encoded string from the authorization header
        """

        if authorization_header is None:
            return None

        if type(authorization_header) != str:
            return None

        if authorization_header[0:6] != "Basic ":
            return None

        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """Decode Base64 encoding
        """

        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) != str:
            return None

        try:
            b64_bytes = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(b64_bytes)
            decoded_val = decoded.decode('utf-8')
            return decoded_val
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extract user credentials from
        decoded base64 authorization header
        """

        default_response = (None, None)
        dec = decoded_base64_authorization_header
        if dec is None:
            return default_response

        if type(dec) != str:
            return default_response

        if ":" not in dec:
            return default_response
        else:
            credentials = dec.split(":")
            return (credentials[0], credentials[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """Retrieve user from the database using credentials
        """

        if user_email is None or type(user_email) != str:
            return None

        if user_pwd is None or type(user_pwd) != str:
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
