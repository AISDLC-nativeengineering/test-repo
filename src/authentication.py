import bcrypt
from datetime import datetime, timedelta
import uuid

# Mock database
users = {
    "example@example.com": {
        "passwordHash": bcrypt.hashpw(b"securepassword123", bcrypt.gensalt()).decode("utf-8"),
    },
}

sessions = {}

def login(email, password):
    user = users.get(email)
    
    if not user or not bcrypt.checkpw(password.encode("utf-8"), user["passwordHash"].encode("utf-8")):
        return {"message": "Invalid credentials"}, None

    # Generate session
    session_id = str(uuid.uuid4())
    expiry = datetime.now() + timedelta(minutes=15)
    sessions[session_id] = {"userId": email, "expiry": expiry}
    return {"message": "Login successful", "token": session_id}, session_id

def validate_session(session_id):
    session = sessions.get(session_id)
    if not session or session["expiry"] < datetime.now():
        return False

    # Extend session
    session["expiry"] = datetime.now() + timedelta(minutes=15)
    return True

# Example test usage
if __name__ == "__main__":
    # Successful login
    response, token = login("example@example.com", "securepassword123")
    print(response)
    print(validate_session(token)) # Extend and validate session

    # Incorrect credentials
    print(login("example@example.com", "wrongpassword"))

    # Session timeout test
    import time
    time.sleep(16 * 60) # Simulate idle for 16 minutes
    print(validate_session(token))