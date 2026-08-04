# A Program to Check if a Character is a Digit.

character = input("Enter a character: ")

if len(character) == 1 and character.isdigit():
    print("Digit")
else:
    print("Not a Digit")
    
# Explanation:
# In this code snippet, we take a character as input from the user. We then check if the length of the input is 1 and if it is a digit character using the isdigit() method. If both conditions are true, we print "Digit". Otherwise, we print "Not a Digit". This code helps in determining whether the entered character is a digit or not.