import streamlit as st
import re
import random

# Blacklisted common passwords
blacklist = [
    "123456", "password", "password123", "123456789", "qwerty", "abc123", "admin", "letmein", "iloveyou", "welcome"
]

# Characters for strong password suggestion
special_chars = "!@#$%^&*"
digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in blacklist:
        return "❌ This password is too common. Please choose another one.", None

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters.")

    # Upper and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use both UPPERCASE and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add a special character (!@#$%^&*).")

    # Final Output
    if score == 4:
        return "Strong Password! You're good to go.", None
    elif score == 3:
        return "Moderate Password - You can still improve it.", suggestions
    else:
        return "Weak Password - Please improve it.", suggestions

# Strong password generator
def generate_strong_password(length=12):
    all_chars = special_chars + digits + lowercase + uppercase
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

# Streamlit App
def main():
    st.title("🔐 Password Strength Meter")

    # User input
    password = st.text_input("Enter your password:")

    if password:
        # Check password strength
        strength_message, suggestions = check_password_strength(password)
        st.write(strength_message)

        if suggestions:
            st.write("Suggestions to improve your password:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")

    # Generate strong password button
    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.write(f"🔒 Suggested Strong Password: {strong_password}")

    st.write("\n---")
    st.write("Built with Streamlit")

# Run the app
if __name__ == "__main__":
    main()