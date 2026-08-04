# A Program to calculate the Sum of all Numeric Values in a Dictionary.

marks = {
    "Math": 88,
    "Physics": 95,
    "Chemistry": 91
}

total = sum(marks.values())

print("Total Marks:", total)

# Explanation:
# The program creates a dictionary containing subject names and marks. The values() method returns all the marks stored in the dictionary. The sum() function then adds every value together and returns the total. That total is stored in the variable 'total' and printed. This provides a quick way to calculate the combined value of all numeric entries.

# Real-Life Use:
# This technique is commonly used to calculate total marks, total expenses, total sales, or any overall numeric result.