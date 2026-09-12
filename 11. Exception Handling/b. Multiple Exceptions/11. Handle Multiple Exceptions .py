# A Program to Handle Multiple Possible Exceptions.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

# Explanation:
# The program first converts the user's input into an integer. ValueError handles invalid input, while ZeroDivisionError handles the case where the user enters zero. Each except block handles a different possible error.

# Real-Life Use:
# Applications often need to handle different types of invalid user input separately so they can provide the correct message.