# A Program to find the Lowest Numeric Value in a Dictionary.

marks = {
    "Math": 88,
    "Physics": 95,
    "Chemistry": 91
}

lowest = min(marks.values())

print("Lowest Marks:", lowest)

# Explanation:
# The program first retrieves all the dictionary values using the values() method. The min() function then compares those values and returns the smallest one. The result is stored in the variable 'lowest' before being displayed on the screen.

# Real-Life Use:
# This operation is useful for identifying the lowest score, minimum price,lowest temperature, or any minimum measurement.