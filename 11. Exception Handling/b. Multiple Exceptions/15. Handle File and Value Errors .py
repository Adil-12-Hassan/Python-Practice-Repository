# A Program to Handle File and Input Errors.

try:
    filename = input("Enter the filename: ")
    number = int(input("Enter a number: "))

    file = open(filename, "r")
    print(f"Number: {number}")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("The requested file was not found.")

except ValueError:
    print("Please enter a valid integer.")

# Explanation:
# The program receives a filename and a number from the user. ValueError handles invalid numeric input, while FileNotFoundError handles a filename that does not exist.

# Real-Life Use:
# Data-processing programs commonly combine file operations with user input, so both types of errors must be handled.