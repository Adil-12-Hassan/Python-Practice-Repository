# A Program to validate marks using raise.

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print(f"Marks: {marks}")

except ValueError as error:
    print(f"Error: {error}")

# Explanation:
# The program converts the input into an integer and checks whether the marks are within the valid range. If the value is outside 0 to 100, raise creates a ValueError with a custom message.

# Real-Life Use:
# Educational systems use validation rules to prevent impossible marks from being stored.