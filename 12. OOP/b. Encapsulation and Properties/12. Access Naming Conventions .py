# A Program to demonstrate Python attribute naming conventions

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")


employee = Employee("Ali", "IT", 80000)

print(employee.name)
print(employee._department)

employee.show_details()


# Explanation:
# name is public and can normally be accessed directly. _department is protected by convention, meaning it is intended for internal use or subclass use. __salary is name-mangled to discourage direct external access. These conventions help communicate how attributes should be used.

# Real-Life Use:
# Naming conventions help developers separate public data from internal implementation details in larger applications.