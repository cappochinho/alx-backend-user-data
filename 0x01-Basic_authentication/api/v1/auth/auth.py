#!/usr/bin/env python3
"""
This file contains the Auth class
"""

from typing import List, TypeVar
from flask import request


class Auth():
    """The Basic authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check
        """

        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path[len(path)-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """

        if request is None:
            return None

        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Undescribed for now
        """

        return None
