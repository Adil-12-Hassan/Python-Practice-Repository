# A Program to Handle an Invalid Object Attribute.

text = "Python"

try:
    print(text.uppercase())

except AttributeError:
    print("The requested attribute or method does not exist.")

# Explanation:
# Python strings provide the upper() method, but they do not provide a method named uppercase(). Python therefore raises AttributeError when the program tries to access it. The except block handles the problem.

# Real-Life Use:
# Attribute errors can occur when working with objects, libraries, and APIs.