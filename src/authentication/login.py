import hashlib

def hash_password(password):
    """Hashes a password using SHA-256 for secure storage."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def login(username, password, user_database):
    """
    Implements the login functionality.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.
        user_database (dict): A dictionary with username as key and hashed password as value.

    Returns:
        str: Success message if login is successful; Error message if unsuccessful.
    """
    hashed_password = hash_password(password)

    if username in user_database:
        if user_database[username] == hashed_password:
            return "Login successful. Welcome, {}!".format(username)
        else:
            return "Error: Invalid credentials."
    return "Error: User not found."

def handle_forgot_password(username):
    """
    Redirect users to password recovery flow.

    Args:
        username (str): The username of the user.

    Returns:
        str: Redirect message to password recovery.
    """
    # Simulated password recovery redirection
    return "Password recovery initiated for {}. Please check your email.".format(username)

def redirect_logged_in_user(username):
    """
    Redirects already logged-in users to the dashboard.

    Args:
        username (str): The username of the logged-in user.

    Returns:
        str: Redirect message to the dashboard.
    """
    return "Welcome back, {}. Redirecting to dashboard...".format(username)