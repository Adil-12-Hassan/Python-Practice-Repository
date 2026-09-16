# A Program to safely process a file.

file = None

try:
    filename = input("Enter the filename: ")
    file = open(filename, "r")
    content = file.read()

except FileNotFoundError:
    print("The file was not found.")

else:
    print("File loaded successfully.")
    print(content)

finally:
    if file is not None:
        file.close()
        print("File closed.")

# Explanation:
# The program receives a filename and attempts to open and read it. If the file does not exist, except handles the error. If reading succeeds, else displays the content. Finally closes the file when it was successfully opened.

# Real-Life Use:
# File-processing applications need safe opening, successful processing, error handling, and proper resource cleanup.