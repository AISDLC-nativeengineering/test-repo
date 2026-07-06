import hashlib
import uuid
from datetime import datetime, timedelta

class ForgotPassword:
    def __init__(self):
        self.reset_links = {}

    def generate_reset_link(self, email):
        """
        Generate a one-time reset link with expiration for 15 minutes.
        """
        reset_token = str(uuid.uuid4())
        expiry_time = datetime.utcnow() + timedelta(minutes=15)

        self.reset_links[reset_token] = {
            'email': email,
            'expiry_time': expiry_time,
            'used': False
        }

        return f"https://example.com/reset-password?token={reset_token}"

    def validate_reset_link(self, token):
        """
        Validate the reset link for expiry and usage.
        """
        link_data = self.reset_links.get(token)
        if not link_data:
            return "Invalid link"

        if link_data['used']:
            return "Link already used"

        if datetime.utcnow() > link_data['expiry_time']:
            return "Link expired"

        return "Valid link"

    def reset_password(self, token, new_password):
        """
        Reset the password if the link is valid.
        """
        validation_status = self.validate_reset_link(token)
        if validation_status != "Valid link":
            return validation_status

        # Mark the link as used
        self.reset_links[token]['used'] = True

        # Update the password securely (example hash storage)
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        # Simulated database update
        print(f"Password for {self.reset_links[token]['email']} updated to {hashed_password}")

        return "Password successfully reset"