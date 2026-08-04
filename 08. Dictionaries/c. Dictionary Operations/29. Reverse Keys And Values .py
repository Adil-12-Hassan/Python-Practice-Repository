# A Program to Reverse the Keys and Values of a Dictionary.

student = {
    "name": "Hasher",
    "course": "Python",
    "city": "Lahore"
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print(reversed_dict)

# Explanation:
# The program first creates an empty dictionary named 'reversed_dict'. The for loop uses items() to retrieve one key-value pair during each iteration. Python stores the current key in the variable 'key' and the current value in the variable 'value'. Inside the loop, these positions are swapped by making the value the new key and the key the new value. After all pairs have been processed, the new reversed dictionary is displayed.

# Real-Life Use:
# Reversing dictionaries is useful when you need fast lookups in the opposite direction, such as finding a user from an ID or a city from a postal code.