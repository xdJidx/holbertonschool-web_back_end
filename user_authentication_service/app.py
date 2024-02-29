#!/usr/bin/env python3
""" Flask module """
from flask import Flask, jsonify, request, abort, redirect, make_response
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """Return a welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    # recup de email et psw depuis les donnees de formulare
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # Tentative d'ajout d'un nouvel user
        user = AUTH.register_user(email, password)
        # succes
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        # si mail deja enregistré
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Sessions Login User """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(401)

    if (AUTH.valid_login(email, pwd)):
        session_id = AUTH.create_session(email)
        if session_id is not None:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """logout function"""
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect("http://localhost:5000/", 302)
    except Exception:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """profile function to respond to the GET /profile route"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": "{}".format(user.email)})


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """Function to respond to the POST /reset_password route"""
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": "{}".format(email),
                        "reset_token": "{}".format(reset_token)})
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_pasword() -> str:
    """Function to respond to the PUT /reset_password route"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": "{}".format(email),
                        "message": "Password updated"}), 200
    except Exception as e:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
