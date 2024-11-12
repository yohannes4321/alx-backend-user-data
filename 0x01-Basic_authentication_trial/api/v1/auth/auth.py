import base64
from typing import TypeVar, List
from models.user import User
from flask import request

class Auth:
    """Base Auth class for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
         
        if excluded_paths is None:
            return True
        val1=excluded_path.split("/")[3]
        normalized_path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            normalized_excluded_path = excluded_path if excluded_path.endswith('/') else excluded_path + '/'
            if normalized_excluded_path.endswith("*"):
                if normalized_path.startswith(normalized_excluded_path[:-1]):
                    return False
            if normalized_excluded_path==normalized_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            print("Authorization header missing")
            return None
        print("Authorization header found:", request.headers['Authorization'])
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        return None