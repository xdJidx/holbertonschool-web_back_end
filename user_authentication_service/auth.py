#!/usr/bin/env python3
"""Auth module
"""

import bcrypt


def _hash_password(password):
    """
    Hashes a password with bcrypt
    
    Args:
        password (str): The password to hash

    Returns:
        bytes: The hashed password
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Return the hashed password as bytes
    return hashed_password


if __name__ == "__main__":
    # Example usage in your main.py
    print(_hash_password("Hello Holberton"))
