# Write a Python program to check if a number is a two-digit number or not.

number = int(input("Enter a number: "))

if (number >= 10 and number <= 99) or (number <= -10 and number >= -99):
    print("Two-Digit Number")
else:
    print("Not a Two-Digit Number")
    
    
# Explanation:
# In this code snippet, we take a number as input from the user and convert it to an integer. We then check if the number is a two-digit number by using logical operators. A two-digit number can be either positive (between 10 and 99) or negative (between -10 and -99). If the condition is true, we print "Two-Digit Number". Otherwise, we print "Not a Two-Digit Number". This code helps in determining whether the entered number is a two-digit number or not.