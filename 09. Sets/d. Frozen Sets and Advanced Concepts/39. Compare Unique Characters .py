# A Program to check whether two strings contain the same unique characters.

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if set(text1) == set(text2):
    print("Both strings contain the same unique characters.")
else:
    print("The strings contain different unique characters.")

# Explanation:
# The program converts both strings into sets. During this conversion, duplicate characters are removed automatically. Python then compares the two sets using the equality operator (==). If both sets contain exactly the same unique characters, the condition becomes True. Otherwise, it returns False.

# Real-Life Use:
# Similar comparisons are used in text analysis, duplicate detection, and validating character sets.