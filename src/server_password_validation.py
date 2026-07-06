# Password Server-side Validation

from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return False, "Password must include at least one number"
    if not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter"
    if not any(char.islower() for char in password):
        return False, "Password must include at least one lowercase letter"
    if not any(char in "!@#$%^&*()" for char in password):
        return False, "Password must include at least one special character"
    return True, "Password is secure"

@app.route('/validate-password', methods=['POST'])
def validate_password_endpoint():
    payload = request.get_json()
    password = payload.get('password', '')
    valid, message = validate_password(password)
    return jsonify({"valid": valid, "message": message})

if __name__ == '__main__':
    app.run(debug=True)