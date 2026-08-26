# A Program to Count the Total Number of Characters in a File.

file = open("notes.txt", "r")
content = file.read()
print("Total Characters:", len(content))
file.close()

# Explanation:
# read() retrieves the complete file contents as a string. The len() function counts all characters in that string, including spaces and newline characters.

# Real-Life Use:
# Useful for text analysis, document processing, and checking text size.