# A Program to initialize objects using __init__()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ali", 20)
student2 = Student("Sara", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)


# Explanation:
# __init__() runs automatically whenever a Student object is created. The name and age values are passed to the constructor. Self refers to the current object being created. The values are stored as instance attributes.

# Real-Life Use:
# __init__() is commonly used to set the initial state of objects, such as creating a customer with a name, email, and account ID.