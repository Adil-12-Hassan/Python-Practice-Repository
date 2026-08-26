# A Program to Read a Specific Number of Characters from a File.

file = open("notes.txt", "r")
content = file.read(10)
print(content)
file.close()

# Explanation:
# The read() method receives 10 as an argument, so only the first 10 characters are read from the file. The selected characters are stored in content and then displayed.

# Real-Life Use:
# Useful when only a small portion of a large file needs to be inspected.