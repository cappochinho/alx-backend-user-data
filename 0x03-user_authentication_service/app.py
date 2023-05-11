#!/usr/bin/env python3
"""Module for the app.py file"""

from flask import Flask, abort, jsonify, redirect, request, make_response
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Entry page"""

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    """Creates a user using the provided arguments"""

    email = request.form.get("email")
    password = request.form.get("password")
    # return jsonify({"email": email, "password": password})
    try:
        AUTH.register_user(email, password)
        return jsonify(
            {
                "email": email,
                "message": "user created"}
        )
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """login into sessions
    """

    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}))
        response.set_cookie('session_id', id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout of a session
    """

    session_id = request.cookies.get("session_id")
    if not session_id or not AUTH.get_user_from_session_id(session_id):
        abort(403)

    AUTH.destroy_session(session_id)
    response = make_response(redirect('/'))
    response.set_cookie('session_id', '', expires=0)
    return response


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """finds the user profile
    """

    session_id = request.cookies.get("session_id")
    if session_id is None or not AUTH.get_user_from_session_id(session_id):
        abort(403)

    email = AUTH.get_user_from_session_id(session_id).email
    if email:
        return (jsonify({"email": email})), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Gets reset password token
    """

    email = request.form.get("email")
    reset_token = AUTH.get_reset_password_token(email)
    if reset_token:
        return jsonify({"email": email, "reset_token": reset_token}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
