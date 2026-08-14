# A Program to count unique words in a paragraph.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
unique_words = set(words)

print("Total Unique Words:", len(unique_words))

# Explanation:
# The program accepts a paragraph from the user and splits it into individual words using the split() method. The resulting list is converted into a set, which automatically removes duplicate words. Finally, the len() function counts the remaining unique words and displays the result.

# Real-Life Use:
# Counting unique words is useful in plagiarism detection, search engines, document analysis, and AI language models.