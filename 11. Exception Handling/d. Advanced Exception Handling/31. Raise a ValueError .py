# A Program to raise a ValueError manually.

age = int(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print(f"Age: {age}")

except ValueError as error:
    print(f"Error: {error}")

# Explanation:
# The program converts the user's input into an integer. If the value is less than zero, raise manually creates a ValueError. The except block catches the error and displays its message.

# Real-Life Use:
# Applications use raise to stop invalid data from continuing through the program.