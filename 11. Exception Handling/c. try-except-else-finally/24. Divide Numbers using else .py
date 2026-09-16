# A Program to perform division using else.

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = first_number / second_number

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

# Explanation:
# The try block converts both inputs and performs division. If conversion or division fails, the matching except block handles the error. The else block runs only when the complete operation succeeds.

# Real-Life Use:
# The else block can separate successful processing from error handling in calculators and data-processing applications.