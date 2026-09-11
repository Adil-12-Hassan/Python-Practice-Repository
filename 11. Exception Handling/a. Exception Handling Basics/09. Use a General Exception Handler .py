# A Program to Handle an Unexpected Exception.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except Exception as error:
    print(f"An error occurred: {error}")

# Explanation:
# Exception catches errors that inherit from Python's general exception hierarchy. The error variable stores the actual exception so the program can display what went wrong.

# Real-Life Use:
# General exception handlers are useful as a final safety layer in larger applications, especially for logging unexpected failures.