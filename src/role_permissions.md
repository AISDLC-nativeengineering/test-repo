# Role-Based Permissions Module

## Description
This module defines role-based permissions for users, allowing administrators to assign roles and control access to specific reports and features.

## Roles
- **Viewer**: Access to view-only reports and restricted features.
- **Analyst**: Access to analytical tools and detailed reports.
- **Manager**: Extended permissions to manage users and reports.
- **Admin**: Full permissions to define roles and configure access.

## Implementation Steps
1. Set up relational database structure:
   - Tables: `roles`, `permissions`, `users_roles`
   - Relationships: Each role has associated permissions.
2. Create API endpoints:
   - `/assign-role`: Assign a role to a user.
   - `/get-permissions`: Retrieve permissions for a user.
3. Add login functionality to enforce role-based access.

## Technical Details
- Use Python and Flask for the backend.
- Store data in a relational database, such as PostgreSQL.