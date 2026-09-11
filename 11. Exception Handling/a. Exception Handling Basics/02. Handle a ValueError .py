# A Program to Handle Invalid Integer Input.

try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}.")

except ValueError:
    print("Please enter a valid integer.")

# Explanation:
# input() returns text, so int() attempts to convert that text into an integer. If the user enters something that cannot be converted, Python raises ValueError and the except block handles it.

# Real-Life Use:
# Forms and applications use this type of validation to prevent invalid numeric data from entering the system.