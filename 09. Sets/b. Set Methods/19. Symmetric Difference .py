# A Program to Find the Symmetric Difference of two Sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print("Symmetric Difference:", result)

# Explanation:
# The program compares two sets using the symmetric_difference() method. Python keeps only the elements that appear in one set but not in both. Common elements are removed from the final result.

# Real-Life Use:
# Symmetric difference helps identify unique customers, products, or records that belong exclusively to one dataset.