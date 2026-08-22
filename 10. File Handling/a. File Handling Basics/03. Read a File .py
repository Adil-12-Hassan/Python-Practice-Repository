# A Program to Read text from a file.

file = open("message.txt", "r")
content = file.read()
file.close()
print(content)

# Explanation:
# The file is opened using "r" mode, which means read mode.
# read() retrieves all the text stored inside the file.
# The returned text is stored in the content variable.
# Finally, close() closes the file.

# Real-Life Use:
# Programs read files to retrieve saved information such as notes, settings, logs, and user data.