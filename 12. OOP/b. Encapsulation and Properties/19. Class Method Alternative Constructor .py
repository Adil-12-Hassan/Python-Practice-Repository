# A Program to use a class method as an alternative constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))


student = Student.from_string("Ali,20")

print(student.name)
print(student.age)


# Explanation:
# The normal constructor expects separate name and age arguments.
# from_string() provides another way to create a Student object. The string is split into separate values.
# cls(name, int(age)) creates and returns a new Student object.

# Real-Life Use:
# Alternative constructors are useful when data comes from files, databases, APIs, configuration files, or user input.