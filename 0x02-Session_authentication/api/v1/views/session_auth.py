#!/usr/bin/env python3
"""Module for the SessionAuth views"""

from os import getenv
from api.v1.views import app_views
from flask import abort, jsonify, request, session
from models.user import User


@app_views.route('/auth_session/login', method=['POST'], strict_slashes=False)
def session_login():
    """Handles session login
    """

    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        abort(jsonify({'error': 'email missing'}), 400)
    if not password:
        abort(jsonify({'error': 'password missing'}), 400)
    user = User.search({'email': email})
    if not user:
        abort(jsonify({'error': 'no user found for this email'}), 404)
    if not user[0].is_valid_password(password):
        abort(jsonify({'error': 'wrong password'}), 401)

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    cookie_name = getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)
    return response


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
)
def auth_session_logout() -> str:
    """
    Logs out a user using session authentication
    """

    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
