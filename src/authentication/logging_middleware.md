# Logging Middleware

This module will track user login history and monitor failed login attempts.

### Features:
- Logs timestamps of all successful user logins.
- Tracks failed login attempts.
- Raises alerts when failed login attempts exceed defined thresholds.

### Implementation:
- Middleware added to the authentication module.
- Database tables created for storing timestamps and counters.