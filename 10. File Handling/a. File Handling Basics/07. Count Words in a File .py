# A Program to Count the Total Number of Words in a File.

file = open("message.txt", "r")
content = file.read()
file.close()
words = content.split()
print("Total Words:", len(words))

# Explanation:
# read() retrieves the complete file content as a string.
# split() separates the text into individual words and stores them in a list.
# len() then counts the number of words in that list.

# Real-Life Use:
# Word counting is commonly used in text analysis, document processing, writing applications, and basic natural language processing.