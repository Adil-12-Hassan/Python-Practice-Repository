# A Program to Manage Student Attendance using Sets.

present_students = set()

while True:

    print("\n===== Student Attendance =====")
    print("1. Mark Attendance")
    print("2. View Present Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")
        present_students.add(name)

    elif choice == "2":

        print("Present Students:", present_students)

    elif choice == "3":

        print("Attendance Closed.")
        break

# Explanation:
# The program creates an empty set to store the names of students who are present. Whenever attendance is marked, the student's name is added using the add() method. Since sets only store unique values, marking attendance multiple times for the same student does not create duplicate entries. The menu continues until the user chooses to exit.

# Real-Life Use:
# Schools and colleges can use sets to ensure each student is counted only once during attendance.