# Forgot Password Functionality

### Description
This script adds a secure `forgot_password` feature allowing users to reset their passwords.

### Features:
- **Public-facing reset page**: Allows email input.
- **Validation**: Confirms email exists in the database.
- **Secure reset link**: Single-use links that expire after 24 hours.
- **New password setting**: Ensures security policies.
- **Rate limiting**: Prevent abuse of reset functionality.
- **Auditing**: Logs reset requests.

### Next Steps
- Integrate SMTP or AWS SES for email functionality.
- Add database operations for email verification and password updates.

---
This module is currently being implemented under the Jira issue AINA-104.