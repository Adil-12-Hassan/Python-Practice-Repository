# A Program to Compare two Sets.

set1 = {1, 2, 3}
set2 = {1, 2, 3}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("The sets are different.")

# Explanation:
# The program creates two sets and compares them using the equality operator (==). Python checks whether both sets contain exactly the same unique elements. The order does not matter because sets are unordered collections. If both sets contain identical elements, the comparison returns True.

# Real-Life Use:
# Comparing sets is useful for verifying whether two datasets, permission groups, or collections contain the same information.