# authentication.py
# Handles secure login and session management for role-based access.

import hashlib
import hmac
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database tables
USERS = {
    "technician1": {"password_hash": "hashed_pw_technician1", "role": "technician"},
    "manager1": {"password_hash": "hashed_pw_manager1", "role": "manager"},
    "it1": {"password_hash": "hashed_pw_it1", "role": "IT"},
}
ROLE_FEATURES = {
    "technician": ["diagnostics", "maintenance-tools"],
    "manager": ["analytics"],
    "IT": ["integration-tools"],
}

def verify_password(username, password):
    user = USERS.get(username)
    if not user:
        return False
    # Mock verify logic
    return hmac.compare_digest(user["password_hash"], hashlib.sha256(password.encode()).hexdigest())

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if verify_password(username, password):
        user_role = USERS[username]["role"]
        features = ROLE_FEATURES.get(user_role, [])
        return jsonify({"token": "mock_token", "role": user_role, "features": features}), 200
    else:
        return jsonify({"error": "Invalid login credentials"}), 401

@app.route('/api/v1/role-data', methods=['GET'])
def role_data():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header.split(" ")[0] != "Bearer":
        return jsonify({"error": "Unauthorized access"}), 401
    # Mock decoding token logic
    user_role = "technician"  # Example decoded token
    data = ROLE_FEATURES.get(user_role, [])
    return jsonify({"role": user_role, "data": data}), 200

if __name__ == "__main__":
    app.run(debug=True)