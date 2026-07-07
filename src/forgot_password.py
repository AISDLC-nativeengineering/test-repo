"""Forgot Password Module."""

import hashlib
import time
import random
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Users database mock
users_db = {
    "user1@example.com": {
        "password": "hashed_password_1"
    },
    "user2@example.com": {
        "password": "hashed_password_2"
    }
}

# Password reset links storage mock
reset_links = {}

# Helper function to generate secure token
def generate_token():
    return hashlib.sha256(f"{random.random()}-{time.time()}".encode()).hexdigest()

# Route to handle "Forgot Password"
@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    email = request.json.get('email')
    if email not in users_db:
        return jsonify({"error": "Invalid email address."}), 404

    # Generate reset link and expiration
    token = generate_token()
    reset_links[token] = {
        "email": email,
        "expires": time.time() + 900  # 15 minutes validity
    }

    # Here, we would send an email containing the link (mocked for this example)
    reset_url = f"http://localhost:5000/reset-password/{token}"
    print(f"Password reset link for {email}: {reset_url}")

    return jsonify({"message": "Password recovery email sent."})

# Route to handle password reset
@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    link_data = reset_links.get(token)

    if not link_data:
        return jsonify({"error": "Invalid or expired reset link."}), 404

    if time.time() > link_data['expires']:
        del reset_links[token]  # Cleanup expired links
        return jsonify({"error": "Expired reset link."}), 410

    if request.method == 'GET':
        return jsonify({"message": "Enter a new password."})

    new_password = request.json.get('new_password')

    if len(new_password) < 8:
        return jsonify({"error": "Password must be at least 8 characters."}), 400

    # Update password in the database
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    users_db[link_data['email']]['password'] = hashed_password

    del reset_links[token]  # Invalidate the token after use

    return jsonify({"message": "Password successfully updated."})

if __name__ == '__main__':
    app.run(debug=True)