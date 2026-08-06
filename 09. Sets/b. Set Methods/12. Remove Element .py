# A Program to Remove an Element from a Set using remove().

fruits = {"Apple", "Banana", "Mango"}
print("Before:", fruits)

fruits.remove("Banana")
print("After:", fruits)

# Explanation:
# The program creates a set and removes the element "Banana" using remove(). Python searches the set for the specified element. If the element exists, it is removed successfully. If it does not exist, Python raises a KeyError, causing the program to stop unless the error is handled.

# Real-Life Use:
# The remove() method is useful when deleting known records that are guaranteed to exist.