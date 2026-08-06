# A Program to find common Elements between two Lists using Sets.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = set(list1).intersection(set(list2))

print("Common Elements:", common)

# Explanation:
# The program converts both lists into sets to remove duplicates. Python then uses the intersection() method to compare the two sets and keeps only the elements that appear in both collections. The resulting set contains all common values.

# Real-Life Use:
# This technique is useful for finding mutual friends, common customers, shared products, or overlapping records.