# A Program to count the Total Number of Lines in a File.

file = open("message.txt", "r")
lines = file.readlines()
file.close()
print("Total Lines:", len(lines))

# Explanation:
# readlines() reads all lines from the file and stores them in a list. Each line becomes one element of the list.
# len() counts how many elements are present, giving us the total number of lines in the file.

# Real-Life Use:
# Line counting can be useful for analysing text files, source code, reports, and log files.