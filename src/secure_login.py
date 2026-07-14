def authenticate_user(username, password):
    valid_users = {"user1": "password123", "user2": "securePassword456"}

    if username in valid_users and valid_users[username] == password:
        return "Authenticated"
    return "Authentication failed"

# Example usage
if __name__ == "__main__":
    user_input_username = input("Enter username: ")
    user_input_password = input("Enter password: ")

    result = authenticate_user(user_input_username, user_input_password)
    print(result)