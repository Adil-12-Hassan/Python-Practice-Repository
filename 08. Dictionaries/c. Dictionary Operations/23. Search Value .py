# A Program to Search for a Value in a Dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

value = input("Enter the value to search: ")

if value in student.values():
    print("Value Found!")
else:
    print("Value Not Found!")

# Explanation:
# The program creates a dictionary and asks the user to enter a value. The values() method returns all the values stored in the dictionary. Python then checks whether the entered value exists among those values. If a match is found, the condition becomes True; otherwise, the else block executes. Unlike key lookups, searching for values requires checking each stored value.

# Real-Life Use:
# This is useful for checking whether a username, course, city, or other piece of information already exists.