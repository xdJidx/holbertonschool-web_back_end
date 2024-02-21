#!/usr/bin/env python3
"""
Use bcrypt to hash a password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to check.

    Returns:
        bool: True if the password matches the hashed password,
          False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
