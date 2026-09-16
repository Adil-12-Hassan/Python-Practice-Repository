# A Program to create and use a class attribute

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Ali")
student2 = Student("Sara")

print(student1.name)
print(student1.school)

print(student2.name)
print(student2.school)


# Explanation:
# school is defined directly inside the Student class. It is a class attribute shared by all Student objects. name is created inside __init__(), so it is an instance attribute. Both objects can access the same school value.

# Real-Life Use:
# Class attributes are useful for shared information, such as a company's name shared by all employees.