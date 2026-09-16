# A Program to use both else and finally.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"Number: {number}")

finally:
    print("Execution finished.")

# Explanation:
# The try block attempts the conversion. If an error occurs, except runs. When there is no error, else runs. Finally runs after either path, making sure its code executes at the end.

# Real-Life Use:
# Applications can use else for successful operations and finally for tasks that must always be completed.