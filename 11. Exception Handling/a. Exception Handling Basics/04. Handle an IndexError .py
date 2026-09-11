# A Program to Handle an Invalid List Index.

numbers = [10, 20, 30]

try:
    print(numbers[6])  # Attempting to access an index that does not exist

except IndexError:
    print("The requested index does not exist.")

# Explanation:
# The list contains only three elements, so index 6 is outside the valid range. Python raises IndexError when the program tries to access it. The except block handles the invalid access.

# Real-Life Use:
# Applications working with lists of records need to handle invalid positions safely.