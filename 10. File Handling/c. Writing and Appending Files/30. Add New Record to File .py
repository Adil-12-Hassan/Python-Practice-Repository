# A Program to Add a New Student Record to an Existing File.

name = input("Enter student name: ")
marks = input("Enter student marks: ")

with open("students.txt", "a") as file:
    file.write(f"Name: {name}, Marks: {marks}\n")

print("Student record added successfully.")

# Explanation:
# The program collects the student's name and marks using input(). The file is opened in append mode so the new record is added without removing previously stored student records. Each student is stored on a new line.

# Real-Life Use:
# This approach can be used for maintaining simple student records, employee records, customer information, or transaction logs.