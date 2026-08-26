# A Program to Count the Number of Lines in a Text File.

file = open("notes.txt", "r")
lines = file.readlines()
print("Total Lines:", len(lines))
file.close()

# Explanation:
# readlines() stores all file lines in a list. The len() function counts how many elements are present in that list, giving the total number of lines in the file.

# Real-Life Use:
# Counting records, entries, or lines in text-based data files.