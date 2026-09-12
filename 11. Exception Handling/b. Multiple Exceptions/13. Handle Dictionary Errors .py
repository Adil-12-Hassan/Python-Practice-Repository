# A Program to Handle Invalid Dictionary Access.

student = {
    "name": "Hasher",
    "age": 21
}

try:
    key = input("Enter a key: ")
    print(student[key])

except KeyError:
    print("That key does not exist.")

# Explanation:
# The user enters a dictionary key, and Python searches for that key inside the dictionary. If the key is missing, Python raises KeyError and the except block handles it.

# Real-Life Use:
# Applications often receive incomplete data, so missing dictionary keys need to be handled safely.