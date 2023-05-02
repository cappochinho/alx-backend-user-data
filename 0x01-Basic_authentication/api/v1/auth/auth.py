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

        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Undescribed for now
        """

        return None
