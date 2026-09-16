# A Program to raise a TypeError for invalid data.

try:
    name = 123

    if not isinstance(name, str):
        raise TypeError("Name must be a string.")

    print(f"Name: {name}")

except TypeError as error:
    print(f"Error: {error}")

# Explanation:
# The program checks the data type of name using isinstance(). Since the value is an integer instead of a string, raise creates a TypeError.

# Real-Life Use:
# Functions and APIs can use type validation to prevent incorrect data types from entering a system.