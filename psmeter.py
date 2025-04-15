import streamlit as st
import re
import random

# Common blacklisted passwords
blacklist = [
    "123456", "password", "password123", "123456789", "qwerty", "abc123", "admin", "letmein", "iloveyou", "welcome"
]

# Character pools for password generation
special_chars = "!@#$%^&*"
digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in blacklist:
        return "❌ This one's way too common. Let's try something better.", None

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Try making your password at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Mix uppercase AND lowercase letters for extra strength.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Throw in a number or two — it helps!")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Special characters like !, @, #, etc. make passwords stronger.")

    if score == 4:
        return "✅ Nailed it! That’s a strong password. 🔐", None
    elif score == 3:
        return "🟡 Not bad, but a few tweaks could make it even better.", suggestions
    else:
        return "🔴 Hmm… that could use some work.", suggestions

# Random strong password generator
def generate_password(length=12):
    if length < 8:
        length = 8  # Minimum length

    # Ensure password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
