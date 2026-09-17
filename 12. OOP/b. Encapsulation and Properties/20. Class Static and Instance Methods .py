# A Program to use instance, class, and static methods together

class Employee:
    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

    @classmethod
    def show_company(cls):
        print(f"Company: {cls.company}")

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


employee = Employee("Ali", 80000)

employee.show_details()
Employee.show_company()

print(Employee.is_valid_salary(80000))


# Explanation:
# show_details() is an instance method because it uses self.
# show_company() is a class method because it uses shared class data.
# is_valid_salary() is a static method because it needs neither instance data nor class data.
# All three method types are used for different responsibilities.

# Real-Life Use:
# Real applications often combine these method types to separate object behavior, class-level operations, and independent utilities.