# A Program to create and use an instance method

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


student = Student("Ali", 20)
student.introduce()


# Explanation:
# The Student object is created with a name and age. introduce() is an instance method because it works with object data. When student.introduce() is called, Python automatically passes the student object as self. The method then accesses the object's name and age attributes.

# Real-Life Use:
# Instance methods represent actions an object can perform, such as a customer placing an order or a car starting.