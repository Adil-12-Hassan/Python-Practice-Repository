# A Program to Convert a Tuple into a Set.

numbers = (10, 20, 30, 20, 40, 30)

number_set = set(numbers)

print("Tuple:", numbers)
print("Set:", number_set)

# Explanation:
# The program creates a tuple that contains duplicate values. The set() function converts the tuple into a set. During the conversion, Python removes all duplicate values automatically because sets only store unique elements. The resulting set is then displayed.

# Real-Life Use:
# This technique is useful when importing data from tuples and removing duplicate entries before further processing.