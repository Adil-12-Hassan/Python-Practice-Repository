# A Program to Move the File Cursor Using seek().

with open("sample.txt", "r") as file:

    file.seek(5)

    data = file.read(10)

    print("Data:", data)

# Explanation:
# The seek() method moves the file cursor to a specific position. Here, the cursor moves to position 5 before reading 10 characters. This allows the program to start reading from a specific location.

# Real-Life Use:
# seek() is useful when a program needs to jump directly to a particular position in a file instead of reading everything from the beginning.