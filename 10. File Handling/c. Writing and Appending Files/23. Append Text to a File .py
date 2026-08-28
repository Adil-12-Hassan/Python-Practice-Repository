# A Program to Append Text to an Existing File.

with open("sample.txt", "a") as file:
    file.write("JavaScript\n")

print("Data appended successfully.")

# Explanation:
# The file is opened using append mode "a". Unlike write mode, append mode does not remove the existing content. The new text is added at the end of the file.

# Real-Life Use:
# Append mode is useful for adding new records, log entries, messages, or other information without deleting existing data.