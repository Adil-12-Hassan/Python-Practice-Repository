# A Program to Handle a Missing File.

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("The file does not exist.")

# Explanation:
# The program attempts to open data.txt in read mode. If the file cannot be found, Python raises FileNotFoundError. The except block catches the error instead of allowing the program to crash.

# Real-Life Use:
# File-based applications must handle missing files when loading saved data.