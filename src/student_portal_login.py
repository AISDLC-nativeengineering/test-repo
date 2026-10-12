# AINA-225
# Implementation of secure student portal login

from hashlib import sha256
import smtplib

def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest()

def authenticate_user(username, password):
    # Replace with actual database call
    user_record = database_lookup(username)

    if not user_record:
        return {'status': 'error', 'message': 'Account does not exist'}

    hashed_password = hash_password(password)

    if user_record['password'] == hashed_password:
        return {'status': 'success', 'session_token': generate_session_token(username)}
    else:
        return {'status': 'error', 'message': 'Invalid username/password'}

def recover_password(email):
    # Validate the email format before attempting recovery
    if not validate_email(email):
        return {'status': 'error', 'message': 'Invalid email format'}

    # Generate recovery instructions and send email
    recovery_link = generate_recovery_link(email)
    send_email(email, f"Password recovery instructions: {recovery_link}")
    return {'status': 'success', 'message': 'Recovery instructions sent'}

def send_email(recipient, content):
    # Replace SMTP setup with actual service
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login('your-email@example.com', 'your-email-password')
        server.sendmail('your-email@example.com', recipient, content)
        server.quit()
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def database_lookup(username):
    # Stub - replace with actual database integration
    users = {
        'student1': {'password': hash_password('password123')},
        'student2': {'password': hash_password('secureP@ssw0rd')}
    }
    return users.get(username)

def validate_email(email):
    return '@' in email and '.' in email

def generate_recovery_link(email):
    # Stub - replace with actual token generation
    return f'https://recovery.example.com/reset?email={email}'

def generate_session_token(username):
    # Stub - replace with actual session handling
    return f'session_token_{username}'}