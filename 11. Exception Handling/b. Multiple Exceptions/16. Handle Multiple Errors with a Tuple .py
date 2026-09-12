# A Program to Handle Multiple Related Exceptions with One Block.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except (ValueError, ZeroDivisionError):
    print("Please enter a valid non-zero number.")

# Explanation:
# ValueError and ZeroDivisionError are grouped inside one tuple. If either exception occurs, Python executes the same except block. This avoids repeating the same handling code.

# Real-Life Use:
# When different errors require the same response, grouping exceptions keeps the program shorter and easier to maintain.