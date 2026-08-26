# A Program to Read All Lines of a File into a List.

file = open("notes.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# Explanation:
# readlines() reads every line from the file and stores the lines inside a list. Each element of the list represents one line from the file.

# Real-Life Use:
# Useful when file data needs to be processed later using list operations.