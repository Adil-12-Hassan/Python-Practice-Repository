# A Program to Read a file using else.

try:
    file = open("data.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("The file was not found.")

else:
    print("File contents:")
    print(content)
    file.close()

# Explanation:
# The try block opens and reads the file. If the file does not exist, FileNotFoundError is handled. If everything succeeds, else displays the file contents and closes the file.

# Real-Life Use:
# Successful file operations can be separated from their error-handling logic using else.