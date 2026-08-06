# A Program to check whether one Set is a Superset of Another.

set1 = {1, 2, 3, 4}
set2 = {1, 2}

result = set1.issuperset(set2)

print("Is Superset:", result)

# Explanation:
# The program creates two sets and uses the issuperset() method. Python checks whether the first set contains every element of the second set. If all elements are present, the method returns True. Otherwise, it returns False.

# Real-Life Use:
# Supersets are useful for verifying that a collection contains everything needed before performing an operation.