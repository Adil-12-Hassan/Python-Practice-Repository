# A Program to Write Multiple Lines into a File.

file = open("notes.txt", "w")

file.write("Python\n")
file.write("NumPy\n")
file.write("PyTorch\n")

file.close()

# Explanation:
# The file is opened in write mode. Three separate strings are written to the file. The \n character moves each new piece of text onto a separate line.

# Real-Life Use:
# Creating structured text files such as lists, logs, and simple reports.