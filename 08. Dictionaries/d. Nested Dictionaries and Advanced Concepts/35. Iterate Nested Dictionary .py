# A Program to Iterate through a Nested Dictionary.

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

for student, details in students.items():
    print(student)

    for key, value in details.items():
        print(f"  {key}: {value}")

# Explanation:
# The outer for loop visits one student record at a time. During each iteration, the variable 'student' stores the student's key (such as "student1"), while 'details' stores the inner dictionary. The inner for loop then iterates through every key-value pair inside that dictionary. This process continues until every student's complete information has been displayed.

# Real-Life Use:
# Nested loops are widely used when displaying database records, API responses, report cards, invoices, and inventory information.