# A Program to Write Text into a File.

file = open("notes.txt", "w")
file.write("Python File Handling.")
file.close()

# Explanation:
# The file is opened in write mode using "w". The write() method places the given text into the file. If the file already contains data, write mode replaces the existing contents.

# Real-Life Use:
# Creating reports, saving generated text, or storing program output.