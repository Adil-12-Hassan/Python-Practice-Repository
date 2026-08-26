# A Program to Copy the Contents of One Text File into Another file.

source = open("source.txt", "r")
content = source.read()
source.close()
destination = open("copy.txt", "w")
destination.write(content)
destination.close()

# Explanation:
# The source file is opened and its complete contents are stored in content. The source file is then closed. A second file is opened in write mode, and the stored contents are written into it.

# Real-Life Use:
# Creating backups or copying information between text files.