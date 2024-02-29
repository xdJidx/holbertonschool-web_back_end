#!/usr/bin/env python3
"""Main file
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def users():
    try:
        # Extract email and password from the form data
        email = request.form['email']
        password = request.form['password']

        # Register the user using the AUTH object
        user = AUTH.register_user(email, password)

        # Respond with a JSON payload for successful registration
        return jsonify({"email": user.email, "message": "user created"}), 200

    except ValueError as e:
        # Catch the exception for already registered user
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
