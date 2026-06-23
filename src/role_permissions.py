"""
role_permissions.py

This module manages role-based permissions for users.
"""

import sqlite3

class RolePermissions:
    def __init__(self, db_path="permissions.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Create the roles and permissions table if it doesn't exist."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS permissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_id INTEGER NOT NULL,
                permission TEXT NOT NULL,
                FOREIGN KEY(role_id) REFERENCES roles(id)
            )"""
        )
        connection.commit()
        connection.close()

    def add_role(self, role_name):
        """Add a new role to the roles table."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO roles (name) VALUES (?)", (role_name,))
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Role '{role_name}' already exists.")
        finally:
            connection.close()

    def add_permission(self, role_name, permission):
        """Add a permission to a role."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            # Get role ID
            cursor.execute("SELECT id FROM roles WHERE name = ?", (role_name,))
            role = cursor.fetchone()
            if role:
                role_id = role[0]
                cursor.execute("INSERT INTO permissions (role_id, permission) VALUES (?, ?)", (role_id, permission))
                connection.commit()
            else:
                print(f"Role '{role_name}' does not exist.")
        except sqlite3.IntegrityError:
            print(f"Permission '{permission}' already exists for role '{role_name}'.")
        finally:
            connection.close()

    def get_permissions(self, role_name):
        """Get all permissions for a given role."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id FROM roles WHERE name = ?", (role_name,))
            role = cursor.fetchone()
            if role:
                role_id = role[0]
                cursor.execute("SELECT permission FROM permissions WHERE role_id = ?", (role_id,))
                permissions = [row[0] for row in cursor.fetchall()]
                return permissions
            else:
                print(f"Role '{role_name}' does not exist.")
                return []
        finally:
            connection.close()

# Example Usage
if __name__ == "__main__":
    rp = RolePermissions()

    # Adding roles
    rp.add_role("viewer")
    rp.add_role("analyst")

    # Adding permissions
    rp.add_permission("viewer", "view_reports")
    rp.add_permission("analyst", "access_analytics")

    # Fetching permissions
    viewer_permissions = rp.get_permissions("viewer")
    analyst_permissions = rp.get_permissions("analyst")
    print("Viewer Permissions:", viewer_permissions)
    print("Analyst Permissions:", analyst_permissions)