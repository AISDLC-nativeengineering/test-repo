import hashlib
import time
import smtplib
from email.mime.text import MIMEText

# Constants for reset token expiry
TOKEN_EXPIRY_MINUTES = 15
PASSWORD_COMPLEXITY = {'min_length': 8, 'special_characters': True}

def send_password_reset_email(email, reset_link):
    """
    Sends a password reset email to the user.
    
    Args:
        email (str): User's email.
        reset_link (str): Secure reset link.
    """
    sender_email = "no-reply@example.com"
    subject = "Password Reset"
    body = f"Click the link to reset your password: {reset_link}\nLink expires in {TOKEN_EXPIRY_MINUTES} minutes."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender_email, "password")
            server.sendmail(sender_email, email, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")


def generate_secure_token(username):
    """
    Generates a secure token for the reset link.
    
    Args:
        username (str): User's username.
    
    Returns:
        str: Secure token.
    """
    current_time = int(time.time())
    data = f"{username}{current_time}"
    return hashlib.sha256(data.encode()).hexdigest()

def validate_password(password):
    """
    Validates password against complexity requirements.
    
    Args:
        password (str): Password to validate.
    
    Returns:
        bool: Whether the password meets complexity requirements.
    """
    if len(password) < PASSWORD_COMPLEXITY['min_length']:
        return False
    if PASSWORD_COMPLEXITY['special_characters']:
        if not any(char in '!@#$%^&*()' for char in password):
            return False
    return True

def handle_password_reset_request(email_or_username):
    """
    Handles password reset request.
    
    Args:
        email_or_username (str): User's email or username.
    """
    reset_link = f"https://example.com/reset?token={generate_secure_token(email_or_username)}"
    send_password_reset_email(email_or_username, reset_link)


# Example usage
if __name__ == "__main__":
    user_input = input("Enter your email or username: \n")
    handle_password_reset_request(user_input)
