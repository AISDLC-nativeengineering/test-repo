import logging

def configure_role_based_access(user_roles, resource_permissions):
    """Configure access permissions based on user roles."""
    for role, permissions in user_roles.items():
        resource_permissions[role] = permissions
    logging.info("Role-based access configured.")


def enable_accessibility_mode(settings, mode):
    """Enable high contrast or screen-reader-friendly mode."""
    if mode == "high_contrast":
        settings['contrast'] = "high"
    elif mode == "screen_reader":
        settings['screen_reader'] = True
    logging.info(f"Accessibility mode '{mode}' enabled.")


def log_unauthorized_access_attempt(user, resource):
    """Log and notify about unauthorized access attempts."""
    logging.warning(f"Unauthorized access attempt by {user} on resource {resource}")
    send_notification(f"Unauthorized access attempt detected for user {user} on resource {resource}")


def send_notification(message):
    """Simulate sending a notification."""
    print(f"NOTIFICATION: {message}")

# Example usage
if __name__ == "__main__":
    user_roles = {"admin": ["view_reports", "edit_dashboard"], "guest": ["view_reports"]}
    resource_permissions = {}
    configure_role_based_access(user_roles, resource_permissions)

    accessibility_settings = {}
    enable_accessibility_mode(accessibility_settings, "high_contrast")

    log_unauthorized_access_attempt("guest", "edit_dashboard")