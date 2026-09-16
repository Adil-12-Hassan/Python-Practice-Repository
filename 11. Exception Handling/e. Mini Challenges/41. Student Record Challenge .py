# A Program to safely create a student record.

class StudentDataError(Exception):
    pass


try:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    if not name.strip():
        raise StudentDataError("Student name cannot be empty.")

    if age <= 0:
        raise StudentDataError("Student age must be positive.")

    if marks < 0 or marks > 100:
        raise StudentDataError("Marks must be between 0 and 100.")

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

except ValueError:
    print("Please enter valid numeric values.")

except StudentDataError as error:
    print(f"Error: {error}")

else:
    print("\nStudent Record")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Marks: {student['marks']}")

# Explanation:
# The program collects the student's name, age, and marks and validates each value. ValueError handles invalid numeric input, while StudentDataError handles application-specific validation rules. The student dictionary is created and displayed only when all validation checks succeed.

# Real-Life Use:
# Student management systems validate and safely store user-provided records.