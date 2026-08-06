# A Program to check whether one Set is a Subset of Another.

set1 = {1, 2}
set2 = {1, 2, 3, 4}

result = set1.issubset(set2)

print("Is Subset:", result)

# Explanation:
# The program creates two sets and uses the issubset() method. Python checks whether every element of the first set exists inside the second set. If all elements are found, the method returns True. If even one element is missing, it returns False.

# Real-Life Use:
# Subsets are useful for checking whether a user has all required permissions, whether required courses have been completed, or whether a shopping list is fully available in stock.