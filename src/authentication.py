# Forgot Password Implementation

from datetime import datetime, timedelta
import hashlib
import smtplib
import random

class ForgotPassword:
    def __init__(self, email_service):
        self.email_service = email_service
        self.tokens = {}

    def request_password_reset(self, email):
        # Generate a unique token
        token = hashlib.sha256(str(random.random()).encode()).hexdigest()
        expiry_time = datetime.now() + timedelta(hours=1)

        self.tokens[token] = {
            'email': email,
            'expires_at': expiry_time
        }

        # Send reset email
        reset_link = f"https://example.com/reset-password?token={token}"
        self.email_service.send_email(
            email,
            "Password Reset Request",
            f"Click the following link to reset your password: {reset_link}\nLink expires at {expiry_time}."
        )

        return "Password reset link sent. Please check your email."

    def reset_password(self, token, new_password):
        # Validate the token
        if token not in self.tokens:
            return "Invalid or expired token."

        token_data = self.tokens[token]
        if datetime.now() > token_data['expires_at']:
            del self.tokens[token]
            return "Token expired. Please request a new password reset link."

        # Perform password complexity check
        if len(new_password) < 8 or not any(char.isdigit() for char in new_password):
            return "Password must be at least 8 characters long and contain a number."

        # Reset password (dummy implementation)
        # Normally, you'd update the password in the database here
        del self.tokens[token]
        return "Password successfully updated."

class EmailService:
    def send_email(self, to_address, subject, content):
        # Dummy email sending logic
        print(f"Sending email to {to_address} with subject '{subject}' and content: {content}")

# Example usage
email_service = EmailService()
forgot_password = ForgotPassword(email_service)

# Requesting a password reset
print(forgot_password.request_password_reset("user@example.com"))

# Resetting the password with a token
print(forgot_password.reset_password("dummy-token", "NewPassword1"))