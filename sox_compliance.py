import logging
from cryptography.fernet import Fernet

class SOXCompliance:
    """
    A module for ensuring SOX regulatory compliance with functionalities
    to generate reports, enforce role-based access control,
    log audit events, and secure sensitive data.
    """

    def __init__(self, encryption_key):
        self.encryption_key = encryption_key
        self.cipher = Fernet(encryption_key)
        logging.basicConfig(
            filename='audit.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def encrypt_data(self, data):
        """Encrypts sensitive data using Fernet encryption."""
        encrypted_data = self.cipher.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypts the encrypted data."""
        return self.cipher.decrypt(encrypted_data).decode()

    def log_event(self, user, event_type, details):
        """Logs access and modification events."""
        logging.info(f"User: {user}, Event: {event_type}, Details: {details}")

    def generate_compliance_report(self):
        """
        Generates a standardized SOX-compliant report including access logs,
        change history, and timestamps.
        """
        with open('audit.log', 'r') as log_file:
            report = log_file.read()
        return report

    def check_permissions(self, user, operation):
        """Validates user permissions for sensitive operations."""
        # Example of role-based check (dummy implementation)
        allowed_roles = ['admin', 'auditor']
        if user.role not in allowed_roles:
            raise PermissionError("Insufficient permissions for this operation.")
        return True

# Example usage
encryption_key = Fernet.generate_key()
sox_compliance = SOXCompliance(encryption_key)

# Log an event
sox_compliance.log_event(user='JohnDoe', event_type='Access', details='Viewed financial report')

# Generate a compliance report
report = sox_compliance.generate_compliance_report()
print("Compliance Report:\n", report)
