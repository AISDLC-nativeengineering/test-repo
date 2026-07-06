# Password Strength Meter - Client-side Implementation

# Provides real-time feedback when the user inputs a password

def calculate_password_strength(password):
    strength = 0

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()" for c in password):
        strength += 1

    return strength

# Simulate feedback as a print for now (integrate with UI later)
def provide_feedback(password):
    strength = calculate_password_strength(password)
    feedback_map = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
    }
    return feedback_map.get(strength, "Invalid Input")

# Example usage:
if __name__ == "__main__":
    sample_password = input("Enter password: ")
    print("Password feedback:", provide_feedback(sample_password))