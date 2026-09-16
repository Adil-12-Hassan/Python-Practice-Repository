# A Program to Demonstrate the complete exception handling flow.

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Program finished.")

# Explanation:
# The try block performs input conversion and division. If an error occurs, the matching except block runs. If no error occurs, else displays the result. Finally runs at the end in both successful and error cases.

# Real-Life Use:
# This structure is useful when an application needs clear success handling, error handling, and guaranteed cleanup.