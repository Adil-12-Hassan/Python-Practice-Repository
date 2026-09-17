# A Program to create a calculated property

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(f"Area: {rectangle.area}")


# Explanation:
# length and width are stored as instance attributes. area is defined as a property instead of storing a separate value. Whenever rectangle.area is accessed, Python calculates the area. This keeps the calculated value synchronized with the dimensions.

# Real-Life Use:
# Calculated properties are useful for values such as totals, discounts, full names, temperatures, or geometric measurements.