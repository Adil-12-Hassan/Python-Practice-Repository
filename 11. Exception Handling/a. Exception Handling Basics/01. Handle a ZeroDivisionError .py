# A Program to Handle Division by Zero.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ZeroDivisionError:
    print("You cannot divide by zero.")

# Explanation:
# The try block attempts to divide 100 by the user's number. If the user enters zero, Python raises a ZeroDivisionError. The except block catches that error and displays a safe message instead of stopping the program.

# Real-Life Use:
# Calculators and financial applications must prevent invalid division operations from crashing the program.