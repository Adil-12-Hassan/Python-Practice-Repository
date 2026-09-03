# A Program to Find the Current Position of the File Cursor.

with open("sample.txt", "r") as file:

    print("Initial position:", file.tell())

    file.read(10)

    print("Position after reading:", file.tell())

# Explanation:
# The tell() method returns the current position of the file cursor. Initially, the cursor is at position 0. After reading 10 characters, the cursor moves forward, and tell() shows its new position.

# Real-Life Use:
# File positions are useful when processing large files or controlling exactly where reading operations should continue.