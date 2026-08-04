# A Program to convert two lists into a Dictionary using zip().

keys = ["name", "age", "course"]
values = ["Hasher", 20, "Python"]

student = dict(zip(keys, values))

print(student)

# Explanation:
# The program creates two separate lists. The zip() function combines the first item from both lists, then the second item, and so on, creating pairs. The dict() function converts these pairs into a dictionary, where the first list becomes the keys and the second list becomes the values.

# Real-Life Use:
# This method is useful when importing data from spreadsheets, CSV files, or databases where keys and values are stored separately.