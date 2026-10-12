# Secure Login Implementation

class SecureLogin:
    def __init__(self):
        pass

    def authenticate_user(self, username, password):
        """Authenticate user credentials."""
        valid_users = {"admin": "password123", "user1": "securePassword456"}
        if username in valid_users and valid_users[username] == password:
            return "Access granted"
        else:
            return "Invalid credentials"

    def forgot_password(self):
        """Display recovery prompts."""
        return "Recovery prompt displayed"

# Simulating valid login
login_system = SecureLogin()
print(login_system.authenticate_user("admin", "password123"))

# Simulating invalid login
print(login_system.authenticate_user("user1", "wrongPassword"))

# Simulating forgot password
print(login_system.forgot_password())