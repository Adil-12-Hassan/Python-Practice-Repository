# A Program to Categorize Age Groups.

age = int(input("\nEnter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
    
# Explanation:
# In this code snippet, we take the user's age as input. We then use if-elif-else statements to categorize the user into different age groups. If the age is 12 or below, we classify them as a "Child". If the age is between 13 and 19, they are classified as a "Teenager". If the age is between 20 and 59, they are classified as an "Adult". Finally, if the age is 60 or above, they are classified as a "Senior Citizen". This code helps in determining the age category of the user based on their input.