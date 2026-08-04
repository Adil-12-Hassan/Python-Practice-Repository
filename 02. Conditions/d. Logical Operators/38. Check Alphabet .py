# A Program to Check if a Character is an Alphabet

character = input("Enter a character: ")

if len(character) == 1 and character.isalpha():
    print("Alphabet")
else:
    print("Not an Alphabet")
    
# Explanation:
# In this code snippet, we take a character as input from the user. We then check if the length of the input is 1 and if it is an alphabet character using the isalpha() method. If both conditions are true, we print "Alphabet". Otherwise, we print "Not an Alphabet". This code helps in determining whether the entered character is an alphabet or not.