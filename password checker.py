def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"

# Test
password = "vcvvdvvsdfsj"
print(check_password_strength(password))

