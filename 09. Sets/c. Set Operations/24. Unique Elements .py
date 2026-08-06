# A Program to find Unique Elements from two Lists.

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

unique = set(list1).symmetric_difference(set(list2))

print("Unique Elements:", unique)

# Explanation:
# The program converts both lists into sets and applies the symmetric_difference() method. Python removes the elements that appear in both collections and keeps only those that exist in exactly one list. The result contains the unique values from both lists.

# Real-Life Use:
# This is useful for comparing customer lists, inventory records, or datasets to identify items that exist in only one source.