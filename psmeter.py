import streamlit as st
import re
import random

# Page config
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Blacklisted common passwords
blacklist = [
    "123456", "password", "password123", "123456789", "qwerty", "abc123", "admin", "letmein", "iloveyou", "welcome"
]

# Characters for strong password suggestion
special_chars = "!@#$%^&*"
digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Password strength checker
def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in blacklist:
        return "❌ This password is too common. Please pick something unique.", None

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make it at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use both **UPPERCASE** and **lowercase** letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include a special character like !, @, # etc.")

    if score == 4:
        return "✅ Strong Password! You're all set. 🔐", None
    elif score == 3:
        return "🟡 Decent effort — just a bit more polish needed.", suggestions
    else:
        return "🔴 Hmm... this could use some serious improvement.", suggestions

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

# --- Streamlit App ---
def main():
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enter your password below to see how secure it really is — and get suggestions too!</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Password input with show/hide toggle
    show_password = st.checkbox("👁 Show password")
    password = st.text_input("Enter your password:", type="default" if show_password else "password", placeholder="Type your password here...")

    if password:
        strength, tips = check_password_strength(password)
        st.markdown(f"<div style='padding: 10px; background-color: #f0f2f6; border-radius: 10px;'>{strength}</div>", unsafe_allow_html=True)

        if tips:
            st.markdown("#### 💡 Suggestions to improve:")
            for tip in tips:
                st.markdown(f"- {tip}")

    st.markdown("---")

    if st.button("✨ Generate Strong Password"):
        generated = generate_strong_password()
        st.markdown(f"""
        <div style='background-color: #dff0d8; padding: 15px; border-radius: 10px; font-size: 16px;'>
            🔒 <strong>Your strong password:</strong><br>
            <code style='font-size: 18px;'>{generated}</code>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: gray;'>Crafted with ❤️ using Streamlit</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
