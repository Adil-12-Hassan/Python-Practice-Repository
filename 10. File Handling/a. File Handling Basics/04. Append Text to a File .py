# A Program to add new text to an Existing File.

file = open("message.txt", "a")
file.write("\nWelcome to Python File Handling.")
file.close()
print("New data added successfully.")

# Explanation:
# The file is opened using "a" mode, which means append mode.
# Append mode adds new data at the end of the existing file without deleting its previous contents.
# The newline character moves the new text onto a new line.

# Real-Life Use:
# Logging systems commonly use append mode to continuously add new information without removing older records.