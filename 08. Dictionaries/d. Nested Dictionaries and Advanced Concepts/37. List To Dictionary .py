# A Program to convert a List into a Dictionary.

fruits = ["Apple", "Banana", "Mango"]

fruit_dict = {}

for index, fruit in enumerate(fruits, start=1):
    fruit_dict[index] = fruit

print(fruit_dict)

# Explanation:
# The program creates a list of fruits and an empty dictionary. The enumerate() function provides both the index and the value during each iteration. The current index becomes the dictionary key, while the fruit name becomes its value. The loop repeats until every list element has been added to the dictionary.

# Real-Life Use:
# This approach is useful when assigning IDs to products, students, or files.