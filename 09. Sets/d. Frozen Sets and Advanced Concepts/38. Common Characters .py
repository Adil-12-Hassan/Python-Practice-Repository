# A Program to find common characters between two strings.

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

common = set(text1).intersection(set(text2))

print("Common Characters:", common)

# Explanation:
# The program converts both strings into sets, where each set contains the unique characters of that string. The intersection() method compares the two sets and returns only the characters that appear in both strings. The result is then displayed.

# Real-Life Use:
# This technique is useful in text comparison, spell checking, and similarity analysis.