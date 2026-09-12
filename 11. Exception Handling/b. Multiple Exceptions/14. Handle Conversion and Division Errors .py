# A Program to Handle Conversion and Division Errors.

try:
    number = float(input("Enter a number: "))
    result = 50 / number
    print(f"Result: {result}")

except ValueError:
    print("Invalid number entered.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Explanation:
# The input is converted into a floating-point number before division. ValueError handles text that cannot become a number, while ZeroDivisionError handles a value of zero.

# Real-Life Use:
# Billing, finance, and calculation systems need to validate numeric input before performing calculations.