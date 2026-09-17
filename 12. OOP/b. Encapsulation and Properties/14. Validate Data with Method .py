# A Program to validate object data through a method

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than zero.")

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")


student = Student("Sara", 20)

student.set_age(21)
student.show_details()

student.set_age(-5)


# Explanation:
# __age stores the student's age internally. set_age() controls changes to the age. The method checks whether the new age is valid before updating it. This prevents invalid values from entering the object's state.

# Real-Life Use:
# Validation methods are useful for protecting application data, such as ages, prices, quantities, account limits, and user settings.