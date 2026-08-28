# A Program to Write Formatted Student Data to a File.

student_name = "Hasher"
student_age = 20
student_course = "Information Technology"

with open("student.txt", "w") as file:
    file.write(f"Name: {student_name}\n")
    file.write(f"Age: {student_age}\n")
    file.write(f"Course: {student_course}\n")

print("Student data saved successfully.")

# Explanation:
# The student's information is stored in separate variables. F-strings are used to combine the variable values with descriptive text. Each piece of information is written on a separate line using "\n".

# Real-Life Use:
# Formatted file writing is useful for saving student records, employee information, reports, and other structured text data.