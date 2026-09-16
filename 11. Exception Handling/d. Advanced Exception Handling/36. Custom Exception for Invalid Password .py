# A Program to create a custom password exception.

class PasswordError(Exception):
    pass


try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise PasswordError("Password must contain at least 8 characters.")

    print("Password accepted.")

except PasswordError as error:
    print(f"Error: {error}")

# Explanation:
# PasswordError is a custom exception created specifically for password validation. If the password contains fewer than eight characters, the program raises this exception and handles it separately.

# Real-Life Use:
# Authentication systems can use custom exceptions for specific validation failures.