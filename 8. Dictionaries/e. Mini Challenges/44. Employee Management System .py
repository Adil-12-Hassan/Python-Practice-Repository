# A Program to manage Employee Records using Dictionaries.

employees = {}

while True:
    print("\n===== Employee Management =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        department = input("Department: ")

        employees[emp_id] = {
            "Name": name,
            "Department": department
        }

    elif choice == "2":
        for emp_id, details in employees.items():
            print(emp_id, "->", details)

    elif choice == "3":
        break

# Explanation:
# The program stores employee records inside a dictionary where each employee ID acts as a unique key. The menu repeatedly asks the user what action to perform. New employees are stored as nested dictionaries containing their details. The program demonstrates how dictionaries organize structured information using unique identifiers.

# Real-Life Use:
# HR systems and company management software commonly organize employee data using dictionaries or database records.