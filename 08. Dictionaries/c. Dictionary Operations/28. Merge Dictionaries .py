# A Program to Merge Two Dictionaries.

student = {
    "name": "Hasher",
    "age": 20
}

details = {
    "course": "Python",
    "city": "Lahore"
}

student.update(details)

print(student)

# Explanation:
# The program creates two separate dictionaries. The update() method reads every key-value pair from the second dictionary and inserts it into the first one. If a key already exists, its value is replaced. Otherwise, Python adds the new key-value pair. After the update is complete, the merged dictionary is printed.

# Real-Life Use:
# Merging dictionaries is useful when combining information collected from multiple forms, databases, or API responses.