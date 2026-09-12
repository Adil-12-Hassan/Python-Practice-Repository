# A Program to Handle List Access Errors.

numbers = [10, 20, 30]

try:
    index = int(input("Enter an index: "))
    print(numbers[index])

except ValueError:
    print("Please enter an integer index.")

except IndexError:
    print("That index does not exist.")

# Explanation:
# The input is converted into an integer and then used as a list index. ValueError handles non-integer input, while IndexError handles an integer that is outside the list's valid index range.

# Real-Life Use:
# Applications that allow users to select records by position need to handle invalid selections safely.