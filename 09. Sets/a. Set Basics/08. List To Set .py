# A Program to Create a Set from a List.

numbers = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = set(numbers)

print("Original List:", numbers)
print("Set:", unique_numbers)

# Explanation:
# The program creates a list containing duplicate values. The set() function converts the list into a set. During this conversion, Python automatically removes all duplicate values and keeps only unique elements. The resulting set is then printed.

# Real-Life Use:
# This technique is commonly used to remove duplicate records from datasets.