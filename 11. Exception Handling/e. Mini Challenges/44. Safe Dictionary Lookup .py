# A Program to safely search for a dictionary key.

student = {
    "name": "Hasher",
    "age": 21,
    "course": "Information Technology"
}

try:
    key = input("Enter key: ")
    print(f"Value: {student[key]}")

except KeyError:
    print("The requested key was not found.")

# Explanation:
# The program receives a key and searches for it in the dictionary. If the key does not exist, Python raises KeyError and the except block handles it.

# Real-Life Use:
# Applications often search user records by keys or field names.