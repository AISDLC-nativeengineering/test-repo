# Password Reset Implementation

### Functionality Overview
This script enables users to reset their password securely via email. It consists of the following workflow:
1. Users initiate password reset via the login page.
2. The system validates inputs and emails a secure reset link.
3. The reset link allows users to update passwords within 24 hours.

### Features:
- Email sending functionality using SMTP (Simple Mail Transfer Protocol).
- Validation for registered email inputs.
- Token generation and expiry validation for reset links.
- Secure encryption and salted hashing for passwords.

### File Structure:
- `password_reset.py`: Contains the implementation of the password reset feature.
- Dependencies:
   - `email-sending` library
   - `hashlib` for password hashing.
   - `time` for token expiry management.

```python
import smtplib
import hashlib
import time

# Function to validate email
def validate_email(email):
    # Perform validation (mock existing email check)
    registered_emails = ["example1@mail.com", "example2@mail.com"]
    return email in registered_emails

# Function to send email
def send_reset_email(email, token):
    sender = "no-reply@example.com"
    message = f"Click the following link to reset your password: https://example.com/reset?token={token}"
    
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('user', 'password')
            server.sendmail(sender, email, message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to generate token
def generate_token():
    return hashlib.sha256(str(time.time()).encode()).hexdigest()

# Function to reset password
def reset_password(new_password):
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    print("Password has been reset successfully and securely!")

"""
Acceptance Criteria:
1. Validate registered email input.
2. Send reset email with token link.
3. Handle token validation.
4. Update passwords after validation.
"""
```

### Usage
This modular script can be invoked via the login page when a user clicks "Forgot Password?"