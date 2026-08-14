# A Program to find unique characters in a string.

text = input("Enter a string: ")

unique_characters = set(text)

print("Unique Characters:", unique_characters)

# Explanation:
# The program asks the user to enter a string and stores it in the variable 'text'. The set() function processes each character one by one. If a character appears multiple times, Python stores it only once because sets allow unique values only. Finally, the set containing all unique characters is displayed.

# Real-Life Use:
# This technique is useful in text analysis, password checking, and Natural Language Processing (NLP).