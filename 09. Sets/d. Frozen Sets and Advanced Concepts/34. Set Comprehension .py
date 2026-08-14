# A Program to create a set using set comprehension.

squares = {number ** 2 for number in range(1, 6)}
print(squares)

# Explanation:
# The program uses set comprehension to create a set in a single line. The variable 'number' takes values from 1 to 5 using the range() function. During each iteration, Python calculates the square of the current number and adds it to the set. After the loop finishes, the completed set of unique squares is displayed.

# Real-Life Use:
# Set comprehensions are useful for generating unique calculated values quickly while writing clean and readable code.