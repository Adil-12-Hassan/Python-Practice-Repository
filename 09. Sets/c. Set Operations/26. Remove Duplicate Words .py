# A Program to Remove Duplicate Words from a Sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique Words:", unique_words)

# Explanation:
# The program asks the user to enter a sentence and splits it into individual words using the split() method. The list of words is then converted into a set, which automatically removes duplicate words. Finally, the unique words are displayed.

# Real-Life Use:
# This approach is useful in text processing, search engines, chatbots, and Natural Language Processing (NLP).