# A Program to Write Text to a File.

with open("sample.txt", "w") as file:
    file.write("Welcome to Python File Handling.")

print("Data written successfully.")

# Explanation:
# The file is opened in write mode using "w". The write() method stores then given text inside the file. If the file already contains data, write mode replaces the existing content with the new text. The with statement automatically closes the file after the operation.

# Real-Life Use:
# Writing files is useful for saving reports, notes, generated information, and other data created by a Python program.