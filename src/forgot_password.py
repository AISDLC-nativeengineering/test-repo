# forgot_password.py
"""
Forgot Password Functionality

This script implements the Forgot Password feature, allowing users to reset their passwords by generating a secure one-time reset link.
"""

import hashlib
import time
import ssl
from email.mime.text import MIMEText
import smtplib

def generate_reset_link(base_url, user_id):
    """
    Generate a secure reset link that expires after 15 minutes.

    :param base_url: Base URL of the system.
    :param user_id: Unique identifier for the user.
    :return: Secure reset link.
    """
    expiry_time = int(time.time()) + 900  # 15 minutes expiration
    data_to_hash = f"{user_id}-{expiry_time}"
    hashed_token = hashlib.sha256(data_to_hash.encode()).hexdigest()
    return f"{base_url}/reset-password?token={hashed_token}&expires={expiry_time}"

def send_email(recipient_email, subject, body):
    """
    Send an email securely using SSL.

    :param recipient_email: Email address of the recipient.
    :param subject: Subject of the email.
    :param body: Body content of the email.
    """
    sender_email = "no-reply@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 465

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, "securepassword")
        server.sendmail(sender_email, recipient_email, msg.as_string())

def validate_reset_link(token, expiry_time):
    """
    Validate the provided reset link.

    :param token: The secure token from the reset link.
    :param expiry_time: The expiration timestamp.
    :return: Boolean indicating whether the link is valid.
    """
    current_time = int(time.time())
    if current_time > expiry_time:
        return False

    # Additional validation logic can be added here
    return True
# Example usage
if __name__ == "__main__":
    user_email = "user@example.com"
    base_url = "https://myapp.com"
    user_id = "12345"

    reset_link = generate_reset_link(base_url, user_id)

    email_subject = "Password Reset Instructions"
    email_body = f"Click the following link to reset your password: {reset_link}\n\nThis link is valid for 15 minutes."

    send_email(user_email, email_subject, email_body)

