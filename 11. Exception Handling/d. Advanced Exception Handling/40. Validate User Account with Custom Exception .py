# A Program to validate a user account with a custom exception.

class AccountError(Exception):
    pass


def validate_account(username, password):

    if not username.strip():
        raise AccountError("Username cannot be empty.")

    if len(password) < 8:
        raise AccountError("Password must contain at least 8 characters.")

    return True


try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    validate_account(username, password)

    print("Account information is valid.")

except AccountError as error:
    print(f"Error: {error}")

# Explanation:
# The validate_account() function checks both username and password. When a validation rule fails, it raises AccountError with a specific message. The main program catches the custom exception and displays the error.

# Real-Life Use:
# Registration systems use validation rules to make sure account information meets the application's requirements before saving it.