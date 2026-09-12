import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a user database for demonstration purposes
USER_DB = {
    "testuser": {
        "username": "testuser",
        "hashedPassword": bcrypt.hashpw("password123".encode(), bcrypt.gensalt()).decode(),
        "isLocked": False,
        "failedAttempts": 0,
        "lastLoginAttempt": None
    }
}

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username not in USER_DB:
        return jsonify({"error": "Invalid username or password."}), 401

    user = USER_DB[username]

    if user['isLocked']:
        return jsonify({"error": "Account is locked. Contact support."}), 423

    if bcrypt.checkpw(password.encode(), user['hashedPassword'].encode()):
        user['failedAttempts'] = 0
        return jsonify({"token": "mock-token", "user": {"id": username, "name": username}})

    user['failedAttempts'] += 1
    if user['failedAttempts'] >= 5:
        user['isLocked'] = True
    return jsonify({"error": "Invalid username or password."}), 401

@app.route('/auth/logout', methods=['POST'])
def logout():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer"):
        return jsonify({"error": "Unauthorized."}), 401

    # Mock logout functionality
    return '', 204

@app.route('/auth/refresh', methods=['POST'])
def refresh():
    data = request.json
    refresh_token = data.get("refreshToken")
    
    if refresh_token != "mock-refresh-token":
        return jsonify({"error": "Invalid or expired refresh token."}), 401

    return jsonify({"token": "new-mock-token"})

if __name__ == '__main__':
    app.run(debug=True)