# This module implements the user login feature

from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for company credentials
COMPANY_USERS = {
    "john.doe@company.com": "securepassword",
    "jane.smith@company.com": "mypassword123",
}

@app.route('/login', methods=['POST'])
def login():
    """Handle user login via single sign-on."""
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email in COMPANY_USERS and COMPANY_USERS[email] == password:
        return jsonify({"status": "success", "message": "Logged in successfully"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid email or password"}), 401

@app.route('/forgot_password', methods=['GET'])
def forgot_password():
    """Provide password recovery options."""
    return jsonify({"status": "success", "message": "Password recovery link has been sent to your email."}), 200

if __name__ == '__main__':
    app.run(debug=True)