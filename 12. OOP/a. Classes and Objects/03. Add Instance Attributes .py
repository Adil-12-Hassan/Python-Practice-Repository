# A Program to add instance attributes to objects

class Student:
    pass


student1 = Student()
student1.name = "Ali"
student1.age = 20

student2 = Student()
student2.name = "Sara"
student2.age = 21

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# Explanation:
# Two Student objects are created. name and age are assigned separately to each object. These are instance attributes because they belong to individual objects. Changing student1 attributes does not change student2 attributes.

# Real-Life Use:
# Instance attributes store data that can be different for each object, such as a student's name, age, ID, or department.