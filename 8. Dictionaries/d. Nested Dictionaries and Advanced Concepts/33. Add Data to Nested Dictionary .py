# A Program to Add Data to a Nested Dictionary.

students = {
    "student1": {
        "name": "Hasher",
        "age": 20
    }
}

students["student1"]["course"] = "Python"

print(students)

# Explanation:
# The program first creates a nested dictionary. Python locates the dictionary stored under the key "student1". A new key named "course" is then created inside that inner dictionary and assigned the value "Python". Finally, the updated nested dictionary is displayed.

# Real-Life Use:
# This technique is useful when adding new information to existing user profiles, employee records, or product details.