# A Program to Count Numeric Values in a Dictionary.

data = {
    "age": 20,
    "marks": 95,
    "course": "Python",
    "city": "Lahore",
    "height": 175
}

count = 0

for value in data.values():
    if isinstance(value, (int, float)):
        count += 1

print("Numeric Values:", count)

# Explanation:
# The program creates a dictionary containing both numbers and text. The for loop iterates through every value returned by the values() method. During each iteration, the variable 'value' stores one dictionary value. The isinstance() function checks whether the value is an integer or a floating-point number. If the condition is True, the counter increases by one. After the loop finishes, the total number of numeric values is displayed.

# Real-Life Use:
# This technique is useful when analyzing mixed datasets containing both text and numerical information.