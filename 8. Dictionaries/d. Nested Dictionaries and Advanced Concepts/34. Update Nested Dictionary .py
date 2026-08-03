# A Program to Update Values in a Nested Dictionary.

students = {
    "student1": {
        "name": "Hasher",
        "age": 20
    }
}

students["student1"]["age"] = 21

print(students)

# Explanation:
# The program creates a nested dictionary and accesses the inner dictionary stored under "student1". Python then finds the key "age" and replaces its current value (20) with the new value (21). After updating the record, the modified nested dictionary is printed.

# Real-Life Use:
# Updating nested dictionaries is common when changing employee information, customer profiles, or student records.