# A Program to validate a password using a custom exception.

class PasswordError(Exception):
    pass


try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise PasswordError("Password must contain at least 8 characters.")

    print("Password is valid.")

except PasswordError as error:
    print(f"Error: {error}")

# Explanation:
# PasswordError is created as a custom exception. The program checks the password length and raises the exception when the password is too short.

# Real-Life Use:
# Registration and login systems validate passwords before accepting accounts.