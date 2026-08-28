# A Program to Append List Items to an Existing File.

new_items = [
    "Webcam",
    "Microphone",
    "Headphones"]

with open("items.txt", "a") as file:

    for item in new_items:
        file.write(item + "\n")

print("New items appended successfully.")

# Explanation:
# The new_items list contains additional values. The for loop processes each item and writes it to the file. Append mode preserves the existing items and places the new items at the end.

# Real-Life Use:
# This method is useful when new products, tasks, users, or records need to be added to an existing collection.