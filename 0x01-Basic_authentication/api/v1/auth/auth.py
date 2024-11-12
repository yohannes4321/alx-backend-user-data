#!/usr/bin/env python3
"""Authentication module for API
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        if excluded_paths is None:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            normalized_excluded_path = (
                excluded_path if excluded_path.endswith('/')
                else excluded_path + '/'
            )
            if normalized_path == normalized_excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        # Check if 'Authorization' header exists and return it
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None

        return None  # User not authenticated
