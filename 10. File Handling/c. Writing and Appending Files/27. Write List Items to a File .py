# A Program to Write List Items to a File.

items = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor"
]

with open("items.txt", "w") as file:

    for item in items:
        file.write(item + "\n")

print("Items saved successfully.")

# Explanation:
# The items list contains several values. The for loop visits each item and writes it to the file. Adding "\n" places every item on a separate line. Write mode creates the file or replaces its previous content.

# Real-Life Use:
# Lists can be stored in files when programs need to save simple collections such as products, tasks, names, or inventory items.