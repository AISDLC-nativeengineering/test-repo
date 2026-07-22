import bcrypt
from datetime import datetime

def signup(email, username, password, additional_info, user_db):
    """
    Creates a new user account.

    Args:
        email (str): Email of the user.
        username (str): Desired username.
        password (str): Desired password.
        additional_info (dict): Additional details about the user.
        user_db (dict): A mock user database.

    Returns:
        dict: User ID and creation timestamp on successful signup.
    """
    # Validate username/email uniqueness
    if username in user_db:
        return {"error": "Username already exists"}

    for user_info in user_db.values():
        if user_info["email"] == email:
            return {"error": "Email already registered"}

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Create user entry
    user_id = f"user_{len(user_db) + 1}"
    user_db[username] = {
        "id": user_id,
        "username": username,
        "email": email,
        "passwordHash": password_hash,
        "additionalInfo": additional_info,
        "createdAt": datetime.utcnow().isoformat(),
    }

    return {"userId": user_id, "createdAt": datetime.utcnow().isoformat()}