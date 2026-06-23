# models.py

class User:
    def __init__(self, user_id, name, department, status="active"):
        self.user_id = user_id
        self.name = name
        self.department = department
        self.status = status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "department": self.department,
            "status": self.status,
        }