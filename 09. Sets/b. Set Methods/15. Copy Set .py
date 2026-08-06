# A Program to Create a Copy of a Set.

fruits = {"Apple", "Banana", "Mango"}

copied_set = fruits.copy()

print("Original Set:", fruits)
print("Copied Set:", copied_set)

# Explanation:
# The program creates a set and then uses the copy() method. Python creates a new set containing the same elements as the original. Both sets are separate objects, so changing one does not affect the other.

# Real-Life Use:
# Copying sets is useful when you need a backup before modifying data.