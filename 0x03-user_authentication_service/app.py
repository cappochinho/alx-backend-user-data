#!/usr/bin/env python3
"""Module for the app.py file"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Entry page"""

    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")