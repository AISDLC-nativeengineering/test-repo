# Reset Password Security Policies

This module handles the secure implementation of resetting passwords based on robust security policies.

## Features:
1. **Real-time Validation:**
   - Validates password complexity (length, special characters).

2. **Recent Password Prevention:**
   - Prevents reuse of recent passwords.

3. **Secure Storage:**
   - Uses salted hashing (bcrypt).

4. **Error Handling:**
   - Lockout mechanism on excessive failed attempts.

5. **Audit Logging:**
   - Logs actions for security trace.

## Technical Notes:
Implemented in Python with focus on:
- Simplicity (regex patterns)
- Performance
- Security

---
## Tests
Unit tests for all functionality are included.