# A Program to Handle an Invalid Operation between Different Data Types.

try:
    number = 10
    text = "10"
    result = number + text
    print(result)

except TypeError:
    print("These data types cannot be combined this way.")

# Explanation:
# The program attempts to add an integer and a string. Python does not allow this operation directly, so it raises TypeError. The except block catches the error and keeps the program running.

# Real-Life Use:
# Data-processing programs often need to handle unexpected data types safely.