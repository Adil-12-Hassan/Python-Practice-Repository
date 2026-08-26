# A Program to Read a Text File Line by Line.

file = open("notes.txt", "r")

for line in file:
    print(line.strip())

file.close()

# Explanation:
# The file is opened in read mode. The for loop goes through the file one line at a time. strip() removes the newline character and extra whitespace from each line before displaying it.

# Real-Life Use:
# Processing large text files without loading the entire file into memory.