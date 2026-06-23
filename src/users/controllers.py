# controllers.py

from models import User

users_db = []  # Mimicking a database

# Create a new user
def create_user(user_id, name, department):
    new_user = User(user_id, name, department)
    users_db.append(new_user)
    return new_user.to_dict()

# Edit an existing user
def edit_user(user_id, name=None, department=None):
    for user in users_db:
        if user.user_id == user_id:
            if name:
                user.name = name
            if department:
                user.department = department
            return user.to_dict()
    return None

# Deactivate a user
def deactivate_user(user_id):
    for user in users_db:
        if user.user_id == user_id:
            user.status = "inactive"
            return user.to_dict()
    return None

# Delete a user
def delete_user(user_id):
    global users_db
    users_db = [user for user in users_db if user.user_id != user_id]
    return True