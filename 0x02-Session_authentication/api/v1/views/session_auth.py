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
    passwd = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not passwd:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for _ in user:
        if not user[0].is_valid_password(passwd):
            return jsonify({"error": "wrong password"}), 401

    if user:
        from api.v1.app import auth
        session_id = auth.create_session(session_id)
        return user.to_json()

    session[getenv('SESSION_NAME')] = session_id
