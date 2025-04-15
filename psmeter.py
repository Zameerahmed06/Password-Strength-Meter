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

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use both UPPERCASE and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add a special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password! You're good to go.", None
    elif score == 3:
        return "⚠️ Moderate Password - You can still improve it.", suggestions
    else:
        return "❌ Weak Password - Please improve it.", suggestions

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
    st.set_page_config(page_title="VIP Password Strength Meter", page_icon="🔐")
    st.title("🔐 VIP Password Strength Checker")

    st.markdown("**Enter your password below to check its strength or generate a secure one!**")

    # Password visibility toggle
    show_password = st.toggle("👁️ Show Password", value=False)

    password = st.text_input("Enter your password:", type='default' if show_password else 'password')

    if password:
        strength_message, suggestions = check_password_strength(password)
        st.markdown(f"### {strength_message}")

        if suggestions:
            st.markdown("#### 💡 Suggestions to improve your password:")
            for suggestion in suggestions:
                st.markdown(f"- {suggestion}")

    st.markdown("---")

    st.markdown("### 🔒 Need Help Creating a Strong Password?")
    pw_length = st.slider("Select password length", 8, 24, 12)
    if st.button("🎲 Generate Strong Password"):
        strong_password = generate_strong_password(pw_length)
        st.success("Here's a secure password you can use:")
        st.code(strong_password, language="text")

    st.markdown("---")
    st.caption("🚀 Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
