# A Program to Demonstrate that a Frozenset is Immutable.

numbers = frozenset({10, 20, 30})

print("Frozen Set:", numbers)

# numbers.add(40)
print("You cannot add or remove elements from a frozenset.")

# Explanation:
# The program creates a frozenset and displays it. The commented line attempts to add a new element using the add() method. If this line is uncommented, Python raises an AttributeError because frozensets are immutable. Their contents cannot be changed after creation.

# Real-Life Use:
# Immutable collections help protect important data from accidental changes during program execution.