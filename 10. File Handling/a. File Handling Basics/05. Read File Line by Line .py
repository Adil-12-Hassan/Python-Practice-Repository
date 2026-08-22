# A Program to Read a File one line at a time.

file = open("message.txt", "r")

for line in file:
    print(line.strip())

file.close()

# Explanation:
# The file is opened in read mode.
# The for loop reads the file one line at a time.
# strip() removes unnecessary whitespace and the newline character.
# After all lines are processed, the file is closed.

# Real-Life Use:
# Reading files line by line is useful when processing large files without loading the entire file into memory at once.