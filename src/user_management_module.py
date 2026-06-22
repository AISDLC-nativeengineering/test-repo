# user_management_module.py

class UserManagement:
    def __init__(self):
        self.roles = {}
        self.users = {}

    def create_role(self, role_name, permissions):
        """Create a role and set permissions."""
        self.roles[role_name] = permissions

    def assign_role(self, user_id, role_name):
        """Assign a role to a specific user."""
        if role_name in self.roles:
            self.users[user_id] = role_name
        else:
            raise ValueError("Role does not exist.")

    def check_permission(self, user_id, permission):
        """Check if a user has a specific permission."""
        role_name = self.users.get(user_id)
        if role_name and permission in self.roles.get(role_name, []):
            return True
        return False