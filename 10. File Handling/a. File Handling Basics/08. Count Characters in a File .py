# A Program to Count the Total Number of Characters in a File.

file = open("message.txt", "r")
content = file.read()
file.close()
print("Total Characters:", len(content))

# Explanation:
# read() loads the complete text from the file into the content variable.
# len() counts every character in that string, including spaces and newline characters if they are present.

# Real-Life Use:
# Character counting can be used for text statistics, input validation, document analysis, and message-length checking.