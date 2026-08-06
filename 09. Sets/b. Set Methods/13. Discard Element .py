# A Program to Remove an Element from a S et using discard().

fruits = {"Apple", "Banana", "Mango"}
print("Before:", fruits)

fruits.discard("Orange")
print("After:", fruits)

# Explanation:
# The program attempts to remove "Orange" using the discard() method. Python checks whether the element exists. Since "Orange" is not present, nothing happens and no error is raised. This makes discard() safer than remove() when you are unsure whether the element exists.

# Real-Life Use:
# discard() is useful when cleaning data where some values may already have been removed.