# A Program to Count Word Frequency using a Dictionary.

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Explanation:
# The program asks the user to enter a sentence and splits it into individual words. An empty dictionary named 'frequency' is created. The loop processes one word at a time. If the word already exists as a key, its count increases by one. Otherwise, get() returns 0, and the word is added with a count of 1. After every word has been processed, the dictionary contains the frequency of each unique word.

# Real-Life Use:
# Word frequency analysis is used in search engines, chatbots, AI, text analytics, and natural language processing.