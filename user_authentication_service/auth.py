#!/usr/bin/env python3
"""Auth module
"""

import bcrypt


def _hash_password(password):
    # Generate a random salt and hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Return the hashed password as bytes
    return hashed_password


if __name__ == "__main__":
    # Example usage in your main.py
    print(_hash_password("Hello Holberton"))
