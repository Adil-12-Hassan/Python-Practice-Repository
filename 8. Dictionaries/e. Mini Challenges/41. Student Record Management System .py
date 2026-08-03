# A Program to manage Student Records using a Dictionary.

students = {}

while True:
    print("\n----- Student Record Management -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        for roll, details in students.items():
            print(f"{roll} -> {details}")

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print(students[roll])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

# Explanation:
# The program creates an empty dictionary named 'students' where each roll number acts as the key and the student's information is stored as a nested dictionary. The while loop keeps displaying the menu until the user chooses to exit. Based on the user's choice, Python adds, displays, searches, or deletes student records. Every operation updates the same dictionary, demonstrating how dictionaries can manage structured data efficiently.

# Real-Life Use:
# Similar systems are used in schools, colleges, coaching centers, and online learning platforms to manage student information.