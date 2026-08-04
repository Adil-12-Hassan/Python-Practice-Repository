# A Program to Count the total number of Key Value pairs in a dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

count = len(student)

print("Total Key-Value Pairs:", count)

# Explanation:
# The program begins by creating a dictionary named 'student' containing three key-value pairs. The len() function is then called with the dictionary as its argument. Python counts every key-value pair stored inside the dictionary and returns the total count. That value is stored in the variable 'count' and then displayed using print(). Unlike lists, the length of a dictionary is determined by the number of keys it contains.

# Real-Life Use:
# This is useful for checking how many records, settings, or fields are stored before processing the data.