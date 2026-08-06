# A Program to Convert a Set into a List.

numbers = {10, 20, 30, 40}

number_list = list(numbers)

print("Set:", numbers)
print("List:", number_list)

# Explanation:
# The program creates a set and converts it into a list using the list() function. Python copies every element from the set into a new list object. Since sets are unordered, the order of elements in the resulting list may vary each time the program runs.

# Real-Life Use:
# This conversion is useful when you need to perform list operations such as indexing, slicing, or sorting on unique data.