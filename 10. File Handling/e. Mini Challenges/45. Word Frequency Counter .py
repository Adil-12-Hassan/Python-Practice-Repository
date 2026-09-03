# A Program to Count How many Times Each Word Appears.

text = "python is easy and python is powerful"

words = text.split()
frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(f"{word}: {count}")

# Explanation:
# split() converts the sentence into individual words. The frequency dictionary stores each word as a key and its number of occurrences as the value. If a word already exists, its count increases by one. Otherwise, the word is added with a count of one.

# Real-Life Use:
# Word-frequency analysis is used in text processing, search systems, Natural Language Processing, and basic data analysis.