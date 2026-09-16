# A Program to create and use a class method

class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(f"School: {cls.school}")


Student.show_school()


# Explanation:
# show_school() is marked with the @classmethod decorator. A class method receives cls instead of self. cls refers to the Student class itself. The method accesses the class attribute school through cls. The method can be called directly using the class name.

# Real-Life Use:
# Class methods are useful when an operation works with shared class-level data instead of a specific object's data.