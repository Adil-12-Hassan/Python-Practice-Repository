# A Program to Handle a Missing Dictionary Key.

student = {
    "name": "Hasher",
    "age": 21
}

try:
    print(student["course"])

except KeyError:
    print("The requested key does not exist.")

# Explanation:
# The dictionary does not contain the key "course". When Python tries to access that missing key, it raises KeyError. The except block catches the error and displays a useful message.

# Real-Life Use:
# APIs and databases often contain missing fields, so programs need to handle missing dictionary keys safely.