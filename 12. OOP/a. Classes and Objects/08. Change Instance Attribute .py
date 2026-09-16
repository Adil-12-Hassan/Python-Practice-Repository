# A Program to change an object's instance attribute

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Ali")

print(student1.name)

student1.name = "Ahmed"

print(student1.name)


# Explanation:
# student1 is created with the name Ali. The name attribute is then changed directly through the object. The original value is replaced with Ahmed. Because name is an instance attribute, this change affects only student1.

# Real-Life Use:
# Object data often changes during program execution, such as updating a customer's address or changing a product's price.