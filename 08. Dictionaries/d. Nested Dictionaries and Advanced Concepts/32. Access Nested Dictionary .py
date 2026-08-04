# A Program to Access values from a Nested Dictionary.

students = {
    "student1": {
        "name": "Hasher",
        "age": 20
    }
}

print("Student Name:", students["student1"]["name"])

# Explanation:
# The program creates a nested dictionary. Python first looks for the key "student1" in the outer dictionary. The value of that key is another dictionary. Python then searches inside this inner dictionary for the key "name" and retrieves its value. Finally, that value is printed on the screen.

# Real-Life Use:
# This method is commonly used when reading JSON data from APIs or accessing detailed information stored inside records.