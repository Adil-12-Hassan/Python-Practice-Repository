# A Program to Safely Process User Input.

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = first_number / second_number

    print(f"Result: {result}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("The second number cannot be zero.")

# Explanation:
# The program converts both inputs into numbers and then performs division. ValueError handles invalid numeric input, while ZeroDivisionError handles the case where the second number is zero.

# Real-Life Use:
# User-facing applications validate input like this to prevent invalid data from causing the program to terminate unexpectedly.