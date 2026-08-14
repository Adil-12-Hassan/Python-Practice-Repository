# A Program to remove duplicate characters from a string.

text = input("Enter a string: ")

result = "".join(set(text))

print("Without Duplicates:", result)

# Explanation:
# The program converts the entered string into a set, automatically removing duplicate characters. The join() method then combines all unique characters into a single string. Since sets are unordered, the characters in the output may appear in a different order than the original string.

# Real-Life Use:
# This method is useful when identifying distinct characters in usernames, passwords, or text datasets.