# A Program to Append User Input to a File.

message = input("Enter a message: ")

with open("messages.txt", "a") as file:
    file.write(message + "\n")

print("Message saved successfully.")

# Explanation:
# The program first receives a message from the user. The file is opened in append mode so the new message is added after the existing messages. The "\n" ensures that the next message starts on a new line.

# Real-Life Use:
# This is useful for storing messages, feedback, notes, comments, or simple activity logs.