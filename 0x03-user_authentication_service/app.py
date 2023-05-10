#!/usr/bin/env python3
"""Module for the app.py file"""

from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
