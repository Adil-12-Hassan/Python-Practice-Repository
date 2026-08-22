# A Program to create a new text file.

file = open("example.txt", "w")
file.close()
print("File created successfully.")

# Explanation:
# The open() function creates a file named "example.txt". The "w" mode means write mode. If the file does not exist, Python creates it. After creating the file, close() closes the file and releases the resource.

# Real-Life Use:
# Programs can create files to store user data, logs, reports, or configuration information.