#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
if getenv("AUTH_TYPE") == "basic_auth":
    auth=BasicAuth()
else:
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    if auth is None:
        return

    public_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                    '/api/v1/forbidden/']
    if auth.require_auth(request.path, public_paths):
        if auth.authorization_header(request) is None:
            abort(401)  # Missing Authorization header
        if auth.current_user(request) is None:
            abort(403)  # Unauthorized user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)