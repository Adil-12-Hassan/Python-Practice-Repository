# A Program to Safely Access Data Inside a Nested Dictionary.

student = {
    "name": "Hasher",
    "details": {
        "age": 21,
        "city": "Lahore"
    }
}

try:
    key = input("Enter a detail key: ")
    print(student["details"][key])

except KeyError:
    print("The requested detail does not exist.")

# Explanation:
# The program first accesses the "details" dictionary and then searches for the user's key inside it. If either dictionary access uses a missing key, KeyError is raised and handled.

# Real-Life Use:
# JSON data from APIs often contains nested dictionaries, where some fields may be missing.