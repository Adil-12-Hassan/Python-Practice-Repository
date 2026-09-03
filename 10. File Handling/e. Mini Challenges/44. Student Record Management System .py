# A Program to Manage Student Records using Dictionaries.

students = {
    "Ali": {"age": 20, "grade": "A"},
    "Ahmed": {"age": 21, "grade": "B"},
    "Sara": {"age": 19, "grade": "A"}
}

for name, details in students.items():

    print(f"Name: {name}")
    print(f"Age: {details['age']}")
    print(f"Grade: {details['grade']}")
    print()

# Explanation:
# The students dictionary stores each student's name as a key. Each value is another dictionary containing the student's age and grade. The loop accesses each student and then reads the information stored inside their nested dictionary.

# Real-Life Use:
# Student management systems use similar structures to store information such as names, grades, attendance, and other academic records.