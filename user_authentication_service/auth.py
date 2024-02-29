#!/usr/bin/env python3
"""
encrypting passwords
"""
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Encrypting passwords using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a UUID for session IDs."""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the Auth class."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the database.
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            # If no user is found, proceed with adding the user
            hashed_password: str = _hash_password(password)
            # Add the new user to the database
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate credentials."""
        try:
            # Retrieve the user by email
            user = self._db.find_user_by(email=email)
            # Check if the provided psw matches the hashed psw in the db
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            # If no user is found with the provided email, return False
            return False

    def create_session(self, email: str) -> str:
        """
        Create a session ID and update it in the database.
        """
        try:
            # Retrieve the user by email
            user = self._db.find_user_by(email=email)
            # Generate a new session ID
            session_id = _generate_uuid()
            # Update the user's session ID in the database
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            # If no user is found with the provided email, return None
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Get user from session ID."""
        if session_id is None:
            # If the session ID is None, return None
            return None

        try:
            # Retrieve the user by session ID
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            # If no user is found with the provided session ID, return None
            return None

    def destroy_session(self, user_id: str) -> None:
        """ Destroy session
        """
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generate reset password token
        """
        if email is None:
            raise ValueError

        try:
            user = self._db.find_user_by(email=email)

            token: str = _generate_uuid()
            self._db.update_user((user.id), reset_token=token)

            return token
        except (NoResultFound, InvalidRequestError):
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update Password
        """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound, InvalidRequestError):
            raise ValueError

        new_passwd = _hash_password(password)

        self._db.update_user(
            (user.id), hashed_password=new_passwd,
            reset_token=None)

        return None
