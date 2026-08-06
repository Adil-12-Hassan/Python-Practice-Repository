# A Program to add Multiple Elements to a Set using update().

fruits = {"Apple", "Banana"}
print("Before:", fruits)

fruits.update(["Mango", "Orange", "Grapes"])
print("After:", fruits)

# Explanation:
# The program creates a set containing two fruits. The update() method is then called with a list of new fruits. Python reads each element from the list one by one and adds it to the set. If an element already exists, it is ignored because sets only store unique values. Finally, the updated set is displayed.

# Real-Life Use:
# The update() method is useful when importing multiple unique records, users, products, or categories into an existing collection.