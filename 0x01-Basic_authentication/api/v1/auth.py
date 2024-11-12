#!/usr/bin/env python3
"""Authentication module for API
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None as the authorization header, for now.
        """
        if request is None:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None, for now, simulating the current user in the
          request.
        """
        if request is None:
            return None
        return None
