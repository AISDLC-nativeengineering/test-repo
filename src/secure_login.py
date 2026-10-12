import smtplib
from email.message import EmailMessage

class UserAuthentication:
    def __init__(self):
        # Simulates a user database for demonstration purposes
        self.users = {
            "user1": "password123",
            "user2": "securePassword456"
        }

    def authenticate_user(self, username, password):
        """Authenticate the user using the username and password."""
        if username in self.users and self.users[username] == password:
            return "Authenticated"
        return "Authentication failed. Invalid username or password."

    def register_user(self, username, password):
        """Register a new user with a username and password."""
        if username in self.users:
            return "Registration failed. Username already exists."
        self.users[username] = password
        return "Registration successful. You can now log in."

    def recover_password(self, username):
        """Send a password recovery email."""
        if username not in self.users:
            return "Password recovery failed. Username not found."

        # Simulate sending email (replace with actual implementation for production)
        recovery_email = "user@example.com"  # Example email, replace in production
        subject = "Password Recovery"
        message = f"Hello {username}, your password is: {self.users[username]}"

        try:
            email = EmailMessage()
            email.set_content(message)
            email["Subject"] = subject
            email["From"] = "noreply@parkingapp.com"
            email["To"] = recovery_email

            # Simulate email sending (use real SMTP configurations in production)
            print(f"Sending email to {recovery_email}:")
            print(f"Subject: {subject}")
            print(f"Message: {message}")
        except Exception as e:
            return f"Password recovery email sending failed: {str(e)}"

        return "Password recovery email sent successfully."

# Example usage
if __name__ == "__main__":
    auth = UserAuthentication()

    # Example operations
    print(auth.authenticate_user("user1", "password123"))
    print(auth.register_user("newuser", "newpassword"))
    print(auth.recover_password("user1"))
