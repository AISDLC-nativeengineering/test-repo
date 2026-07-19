import hashlib
import re

def hash_password(password):
    """Hash a password for secure storage."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def is_password_strong(password):
    """Enforce strong password requirements."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@$!%*?&#]", password):
        return False
    return True

def send_reset_email(user_email, reset_link):
    """Simulate sending a password reset email."""
    print(f"Password reset link sent to {user_email}: {reset_link}")

def reset_password(username, new_password):
    """Reset the user's password if it meets the requirements."""
    if not is_password_strong(new_password):
        raise ValueError('Password must be stronger.')
    hashed_password = hash_password(new_password)
    # Simulate saving hashed password to the database
    print(f"Password for {username} has been updated and hashed as {hashed_password}.")