# A Program to Remove Duplicate Values from a List using a Set.

numbers = [10, 20, 30, 20, 40, 30, 50]
print("Original List:", numbers)

unique_numbers = list(set(numbers))
print("List Without Duplicates:", unique_numbers)

# Explanation:
# The program begins with a list that contains duplicate values. First, the set() function converts the list into a set, automatically removing repeated elements because sets only store unique values. The set is then converted back into a list using the list() function. Finally, the updated list without duplicate values is displayed.

# Real-Life Use:
# This method is useful for cleaning datasets, removing duplicate IDs, usernames, phone numbers, or email addresses.