# A Program to Demonstrate that finally always executes.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Thank you for using the program.")

# Explanation:
# The program may encounter ValueError or ZeroDivisionError during execution. The appropriate except block handles the error, but finally still runs after the exception-handling process.

# Real-Life Use:
# Programs use finally for actions such as displaying completion messages or releasing resources that must happen regardless of success or failure.