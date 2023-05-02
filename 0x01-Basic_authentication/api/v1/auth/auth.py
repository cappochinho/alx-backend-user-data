#!/usr/bin/env python3
"""
This file contains the Auth class
"""

from typing import List, TypeVar
from flask import request


class Auth():
    """The authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Undescribed
        Returns just False for now
        """

        if path is None:
            return True

        if excluded_paths == None or excluded_paths == []:
            return True

        if path[len(path)-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Undescribed for now
        """

        return None
