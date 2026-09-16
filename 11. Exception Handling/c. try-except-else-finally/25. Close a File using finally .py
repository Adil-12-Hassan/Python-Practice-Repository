# A Program to Close a file using finally.

file = None

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("The file was not found.")

finally:
    if file is not None:
        file.close()
        print("File closed.")

# Explanation:
# The file variable starts as None because the file may not open successfully. If the file opens, its contents are read. Finally checks whether the file was opened and closes it when necessary.

# Real-Life Use:
# Files and other resources should be closed properly to prevent resource leaks and locked files.