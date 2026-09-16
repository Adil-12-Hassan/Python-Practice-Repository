# A Program to Use finally with exception handling.

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")

# Explanation:
# The try block attempts to convert the input into an integer. If conversion fails, except handles the error. The finally block runs in both cases, whether an exception occurs or not.

# Real-Life Use:
# finally is commonly used for cleanup tasks such as closing files or releasing resources.