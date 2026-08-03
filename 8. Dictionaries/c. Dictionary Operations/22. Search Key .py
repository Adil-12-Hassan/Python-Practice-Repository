# A Program to Search for a Key in a Dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

key = input("Enter the key to search: ")

if key in student:
    print("Key Found!")
else:
    print("Key Not Found!")

# Explanation:
# The program first creates a dictionary and then asks the user to enter a key. Whatever the user types is stored in the variable 'key'. The 'in' operator checks whether that key exists in the dictionary. If Python finds the key, the condition becomes True and the first message is printed. Otherwise, the else block executes. Searching by keys is very fast because dictionaries are designed for quick key lookups.

# Real-Life Use:
# Searching for keys is commonly used in login systems, APIs, and configuration files before retrieving data.