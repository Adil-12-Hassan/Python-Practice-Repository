# A Program to Find the Difference between two Sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)

print("Difference:", result)

# Explanation:
# The program compares two sets using the difference() method. Python checks every element in the first set. If an element is not found in the second set, it is included in the result. Elements common to both sets are excluded.

# Real-Life Use:
# Difference is useful for finding students who are absent, products that are out of stock, or users missing from another database.