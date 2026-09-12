# A Program to Build a Calculator with Multiple Exception Handling.

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    else:
        raise ValueError("Invalid operator.")

    print(f"Result: {result}")

except ValueError as error:
    print(f"Input error: {error}")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Explanation:
# The program receives two numbers and an operator, then selects the correct calculation. ValueError handles invalid numbers or operators, while ZeroDivisionError handles division by zero.

# Real-Life Use:
# Real calculators and financial applications validate user input and handle calculation errors instead of allowing the application to crash.