# A Program to create a safe calculator.

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

except ValueError as error:
    print(f"Error: {error}")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Calculator finished.")

# Explanation:
# The program receives two numbers and an operator, then performs the selected calculation. ValueError handles invalid input or operators, while ZeroDivisionError handles division by zero. Else displays successful results, and finally always displays the completion message.

# Real-Life Use:
# Calculator applications need input validation and safe handling of calculation errors.