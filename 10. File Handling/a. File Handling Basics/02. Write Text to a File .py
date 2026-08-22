# A Program to write text into a file.

file = open("message.txt", "w")
file.write("Hello, Python!")
file.close()
print("Data written successfully.")

# Explanation:
# The file is opened using "w" mode, which allows Python to write data.
# write() places the given text inside the file.
# close() finishes the operation and closes the file.

# Real-Life Use:
# Applications can save messages, reports, notes, and other text data into files.