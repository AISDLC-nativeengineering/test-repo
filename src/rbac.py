"""
Role-Based Access Control (RBAC) Implementation

This module defines and enforces roles and permissions
for the financial dashboard.
"""

# Define roles
ROLES = {
    "Admin": {
        "access_dashboard_settings": True,
        "generate_reports": True,
        "approve_workflows": True,
        "view_reports": True,
    },
    "Manager": {
        "access_dashboard_settings": False,
        "generate_reports": True,
        "approve_workflows": True,
        "view_reports": True,
    },
    "Viewer": {
        "access_dashboard_settings": False,
        "generate_reports": False,
        "approve_workflows": False,
        "view_reports": True,
    },
}

# Audit log
AUDIT_LOG = []

def enforce_permissions(user_role, action):
    """
    Enforce RBAC permissions.

    Parameters:
        user_role (str): Role of the user (Admin, Manager, Viewer).
        action (str): Action user wants to perform.

    Returns:
        bool: True if permission granted, False otherwise.
    """
    if user_role not in ROLES:
        AUDIT_LOG.append(f"Access denied for unknown role: {user_role}")
        return False

    permissions = ROLES[user_role]

    if action in permissions and permissions[action]:
        AUDIT_LOG.append(f"Access granted for role: {user_role}, Action: {action}")
        return True
    else:
        AUDIT_LOG.append(f"Access denied for role: {user_role}, Action: {action}")
        return False

def edit_permissions(admin_role, role_to_edit, new_permissions):
    """
    Allow Admins to edit permissions for other roles.

    Parameters:
        admin_role (str): Role of the user (should be 'Admin').
        role_to_edit (str): Role to modify.
        new_permissions (dict): Updated permissions.

    Returns:
        bool: True if changes are successful, False otherwise.
    """
    if admin_role != "Admin":
        AUDIT_LOG.append(f"Permission modification denied for non-admin role: {admin_role}")
        return False

    if role_to_edit in ROLES:
        ROLES[role_to_edit] = new_permissions
        AUDIT_LOG.append(f"Permissions updated for {role_to_edit} by {admin_role}")
        return True

    AUDIT_LOG.append(f"Attempt to edit unknown role {role_to_edit} by {admin_role}")
    return False

def get_audit_log():
    """
    Retrieve the audit log.

    Returns:
        list: List of audit log entries.
    """
    return AUDIT_LOG

# Example usage:
# enforce_permissions("Manager", "generate_reports")
# edit_permissions("Admin", "Viewer", {"access_dashboard_settings": False})
