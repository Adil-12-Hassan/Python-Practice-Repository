# A Program to Remove and Return a Random Element using pop().

fruits = {"Apple", "Banana", "Mango"}

print("Before:", fruits)

removed = fruits.pop()

print("Removed Element:", removed)
print("After:", fruits)

# Explanation:
# The program creates a set and calls the pop() method. Because sets are unordered, Python removes and returns an arbitrary element rather than a specific one. The removed element is stored in the variable 'removed', and the remaining set is displayed afterward.

# Real-Life Use:
# The pop() method is useful when processing or consuming unique items without caring about their order.