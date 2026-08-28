# A Program to Write User Input to a File.

name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("User information saved successfully.")

# Explanation:
# The input() function collects the user's name and age. These values are stored in variables and then written into user.txt using f-strings. The "\n" places the name and age on separate lines.

# Real-Life Use:
# Programs can use this technique to save user information, preferences, registration details, or simple records.