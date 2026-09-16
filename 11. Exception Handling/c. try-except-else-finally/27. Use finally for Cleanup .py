# A Program to perform cleanup with finally.

resource_open = False

try:
    print("Opening resource...")
    resource_open = True

    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except ValueError:
    print("Invalid input.")

finally:
    if resource_open:
        print("Closing resource.")
        resource_open = False

# Explanation:
# The program uses a Boolean variable to track whether a resource was opened. Finally checks that state and performs cleanup regardless of whether an exception occurred.

# Real-Life Use:
# Cleanup logic is important when working with files, database connections, network connections, and other resources.