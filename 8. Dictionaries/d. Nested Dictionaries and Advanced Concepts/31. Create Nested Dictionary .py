# A Program to create a Nested Dictionary.

students = {
    "student1": {
        "name": "Hasher",
        "age": 20
    },
    "student2": {
        "name": "Ali",
        "age": 22
    }
}

print(students)

# Explanation:
# The program creates a nested dictionary named 'students'. The outer dictionary contains two keys: "student1" and "student2". Instead of storing simple values, each key stores another dictionary. These inner dictionaries contain the student's name and age. When print() is called, Python displays the complete nested structure. Nested dictionaries are useful when each record contains multiple pieces of related information.

# Real-Life Use:
# Nested dictionaries are used in databases, school management systems,employee records, APIs, and JSON data where one object contains multiple properties.