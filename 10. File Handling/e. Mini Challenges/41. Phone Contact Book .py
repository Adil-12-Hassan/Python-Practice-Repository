# A Program to Create and Search a Phone Contact Book.

contacts = {
    "Ali": "0300-1234567",
    "Ahmed": "0311-1234567",
    "Sara": "0322-1234567"
}

name = input("Enter contact name: ")

if name in contacts:
    print(f"{name}'s phone number: {contacts[name]}")
else:
    print("Contact not found.")

# Explanation:
# The contacts dictionary stores names as keys and phone numbers as values. The program takes a name from the user and checks whether that name exists in the dictionary. If it exists, its phone number is displayed.

# Real-Life Use:
# Contact applications use similar key-value relationships to associate people's names with their contact information.