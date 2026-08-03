# A Program to manage Library Books using Dictionaries.

library = {
    "Python": True,
    "Java": False,
    "C++": True
}

for book, available in library.items():

    if available:
        status = "Available"
    else:
        status = "Issued"

    print(f"{book} : {status}")

# Explanation:
# The dictionary stores book names as keys and their availability as Boolean values. The loop checks each book one by one. If the value is True, Python displays "Available"; otherwise, it displays "Issued". This demonstrates how dictionaries can represent the status of different items.

# Real-Life Use:
# Libraries use similar logic to keep track of which books are available and which have already been borrowed.