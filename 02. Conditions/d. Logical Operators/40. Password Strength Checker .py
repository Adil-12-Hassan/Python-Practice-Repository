# A Program to Check Password Strength.

password = input("Enter your password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
    
# Explanation:
# In this code snippet, we take a password as input from the user. We then check if the length of the password is greater than or equal to 8 using an if statement. If the condition is true, we print "Strong Password". Otherwise, we print "Weak Password". This code helps in determining the strength of the entered password based on its length.