# A Program to create a property getter

class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


student = Student("Ali")

print(student.name)


# Explanation:
# __name stores the actual value internally. The name() method is converted into a property using @property. This allows the method to be accessed like a normal attribute.
# 'student.name' automatically calls the property getter.

# Real-Life Use:
# Properties are useful when you want attribute-like access while keeping control over how data is retrieved or calculated.