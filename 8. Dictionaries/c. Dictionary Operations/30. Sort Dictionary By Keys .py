# A Program to Sort a Dictionary by its Keys.

student = {
    "course": "Python",
    "city": "Lahore",
    "age": 20,
    "name": "Hasher"
}

sorted_dict = dict(sorted(student.items()))

print(sorted_dict)

# Explanation:
# The program begins by retrieving all key-value pairs using the items() method. The sorted() function arranges these pairs in alphabetical order based on their keys. Since sorted() returns a list of tuples, the dict() function converts that list back into a dictionary. The sorted dictionary is then printed, showing the keys in ascending alphabetical order.

# Real-Life Use:
# Sorting dictionary keys makes reports, configuration files, and displayed information easier to read and organize.