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
