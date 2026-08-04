# A Program to Print the Multiplication Table of the Number Given by the User.

number = int(input("\nEnter a number: "))

print(f"\nTable of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Explanation:
# This code snippet prompts the user to enter a number and then prints the multiplication table for that number from 1 to 10. It uses a for loop to iterate through the numbers 1 to 10, multiplying the user-provided number by the current iteration value (i) and printing the result in a formatted string. This demonstrates how to use a for loop to generate and display a multiplication table based on user input.