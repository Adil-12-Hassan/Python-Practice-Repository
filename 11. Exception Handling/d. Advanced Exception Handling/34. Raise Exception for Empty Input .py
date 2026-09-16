# A Program to prevent empty user input.

try:
    name = input("Enter your name: ")

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    print(f"Hello, {name}!")

except ValueError as error:
    print(f"Error: {error}")

# Explanation:
# The program receives the user's name and removes surrounding spaces with strip(). If nothing remains, raise creates a ValueError. Otherwise, the program continues and displays the name.

# Real-Life Use:
# Forms use similar validation to prevent required fields from being empty.