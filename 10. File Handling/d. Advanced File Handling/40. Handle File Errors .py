# A Program to Handle File Errors Safely.

try:

    with open("missing_file.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

# Explanation:
# The try block contains the file operation that might fail. If the requested file does not exist, Python raises FileNotFoundError. The except block catches that error and displays a friendly message instead of allowing the program to terminate unexpectedly.

# Real-Life Use:
# Error handling is important in real applications because files can be missing, moved, renamed, or inaccessible. Handling errors makes programs more reliable and user-friendly.