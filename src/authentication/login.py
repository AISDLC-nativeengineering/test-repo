import bcrypt
import jwt
import os
from datetime import datetime, timedelta

# Replace SECRET_KEY with secure storage in production
SECRET_KEY = "your_secret_key"
JWT_EXPIRATION_HOURS = 1

def login(username, password, user_db):
    """
    Authenticates a user based on username and password.

    Args:
        username (str): The username of the user.
        password (str): The password provided by the user.
        user_db (dict): A mock user database.

    Returns:
        dict: Token and expiry details on successful login, or error message.
    """
    # Fetch user details
    user = user_db.get(username)
    if not user:
        return {"error": "Invalid username or password"}

    # Verify password
    if not bcrypt.checkpw(password.encode(), user["passwordHash"].encode()):
        return {"error": "Invalid username or password"}

    # Generate JWT Token
    expiry = datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS)
    token = jwt.encode({"username": username, "exp": expiry}, SECRET_KEY, algorithm="HS256")

    return {"token": token, "expiry": expiry.isoformat()}