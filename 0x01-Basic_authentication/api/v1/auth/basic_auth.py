#!/usr/bin/env python3
"""
Contains the class BasicAuth, that inherits from Auth
"""

from api.v1.auth.auth import Auth


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
