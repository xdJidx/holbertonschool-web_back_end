#!/usr/bin/env python3
"""Auth module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password):
        """Register a new user in the database.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The User object representing the added user.
        """
        try:
            # Check if the user already exists in the database
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            # If no user is found with the email, proceed with registration
            # Hash the password using the _hash_password
            # method (assuming it exists)
            hashed_password = self._hash_password(password)

            # Create a new User object
            new_user = self._db.add_user(email, hashed_password)

            # Return the User object
            return new_user

    def _hash_password(self, password):
        # Implement your password hashing logic here (use bcrypt, for example)
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password