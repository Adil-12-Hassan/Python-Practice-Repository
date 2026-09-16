# A Program to Use else with try-except.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid integer.")

else:
    print(f"You entered: {number}")

# Explanation:
# The try block attempts to convert the user's input into an integer. If the conversion fails, except handles the ValueError. If no error occurs, the else block runs and displays the entered number.

# Real-Life Use:
# The else block is useful when some code should run only after an operation completes successfully.