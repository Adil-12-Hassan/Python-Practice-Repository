# A Program to create a custom exception.

class AgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("You must be at least 18 years old.")

    print("Age accepted.")

except AgeError as error:
    print(f"Error: {error}")

# Explanation:
# AgeError inherits from Python's built-in Exception class, creating a custom exception type. When the age is below 18, the program raises AgeError and the matching except block handles it.

# Real-Life Use:
# Custom exceptions make application-specific validation errors easier to identify and handle.