# A Program to Add New Text to the End of a File.

file = open("notes.txt", "a")
file.write("\nFile Handling")
file.close()

# Explanation:
# The file is opened in append mode using "a". Unlike write mode, append mode keeps the existing contents and adds the new text at the end of the file.

# Real-Life Use:
# Adding new records, messages, or entries to an existing file.