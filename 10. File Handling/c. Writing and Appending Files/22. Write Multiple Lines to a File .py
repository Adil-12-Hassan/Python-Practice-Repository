# A Program to Write Multiple Lines to a File.

with open("sample.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")

print("Multiple lines written successfully.")

# Explanation:
# The write() method is called multiple times to store different lines. The "\n" character moves the following text to a new line. Since the file is opened in write mode, any previous content is replaced.

# Real-Life Use:
# Multiple lines can be used to store lists, records, names, tasks, or other information that needs to be organized line by line.