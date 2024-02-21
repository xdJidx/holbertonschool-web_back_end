#!/usr/bin/env python3
"""
Use bcrypt to hash a password
"""

import bcrypt

def hash_password(password: str) -> bytes:
    # Generate a random salt
    salt = bcrypt.gensalt()
    
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password
