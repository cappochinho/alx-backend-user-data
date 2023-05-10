#!/usr/bin/env python3
"""Module for the app.py file"""

from flask import Flask, abort, jsonify, request, make_response
from auth import Auth
import os

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
        response = make_response()
        response.set_cookie('session_id', id)
        return jsonify({"email": "<user email>", "message": "logged in"})
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
