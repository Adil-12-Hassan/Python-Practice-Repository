# A Program to Copy Content from one File to Another.

with open("sample.txt", "r") as source:
    content = source.read()

with open("backup.txt", "w") as destination:
    destination.write(content)

print("File copied successfully.")

# Explanation:
# The source file is opened in read mode and its complete content is stored in the content variable. A second file is opened in write mode, and the same content is written into it. This creates a copy of the original data.

# Real-Life Use:
# Copying files is useful for creating backups, duplicating reports, or transferring stored text data.