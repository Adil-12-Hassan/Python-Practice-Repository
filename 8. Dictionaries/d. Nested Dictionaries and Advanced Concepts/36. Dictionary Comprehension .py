# A Program to create a Dictionary using Dictionary Comprehension.

squares = {number: number ** 2 for number in range(1, 6)}

print(squares)

# Explanation:
# The program uses dictionary comprehension to create a dictionary in a single line. The loop starts with the number 1 and continues until 5. During each iteration, the current value is stored in the variable 'number'. That number becomes the dictionary key, while its square becomes the corresponding value. After the loop finishes, Python returns the completed dictionary.

# Real-Life Use:
# Dictionary comprehensions are useful for quickly generating mappings, lookup tables, and processed datasets.