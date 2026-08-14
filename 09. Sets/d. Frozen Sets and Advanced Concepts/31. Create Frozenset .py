# A Program to create a frozenset.

numbers = frozenset({10, 20, 30, 40})

print("Frozen Set:", numbers)

# Explanation:
# The program creates a normal set containing four numbers and passes it to the frozenset() function. Python creates a new immutable set, meaning its elements cannot be added, removed, or modified after creation. The resulting frozenset is then displayed using the print() function.

# Real-Life Use:
# Frozensets are useful when data should remain constant, such as predefined permissions, configuration values, or fixed categories.