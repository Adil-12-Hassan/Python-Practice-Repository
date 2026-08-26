# A Program to Read the Entire Contents of a Text File.

file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

# Explanation:
# The file is opened in read mode using "r". The read() method reads the complete contents of the file and stores them in the content variable.
# The contents are then displayed using print(). Finally, close() releases the file resource.

# Real-Life Use:
# Reading configuration files, notes, reports, or stored text data.