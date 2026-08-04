# A Program to find the Highest Numeric Value in a Dictionary.

marks = {
    "Math": 88,
    "Physics": 95,
    "Chemistry": 91
}

highest = max(marks.values())

print("Highest Marks:", highest)

# Explanation:
# The program creates a dictionary where each subject is stored as a key and its marks are stored as the value. The values() method retrieves all the marks, and the max() function compares them to find the largest value. The highest value is stored in the variable 'highest' and then printed.

# Real-Life Use:
# Finding the highest value is useful for determining top scores, highest sales, maximum temperatures, and similar analyses.