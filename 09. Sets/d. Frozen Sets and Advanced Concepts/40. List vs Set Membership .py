# A Program to compare membership testing in a list and a set.

numbers_list = list(range(1, 100001))
numbers_set = set(numbers_list)

target = 99999

print("List Result:", target in numbers_list)
print("Set Result:", target in numbers_set)

# Explanation:
# The program creates both a list and a set containing the same numbers. The 'in' operator checks whether the target value exists in each collection. Both searches return the same result, but internally they work differently. A list usually checks elements one by one until it finds the target, while a set uses hashing to locate elements much more efficiently. Although the output is identical, membership testing is generally much faster in a set, especially when working with very large collections of data.

# Real-Life Use:
# Sets are preferred over lists for fast lookups in applications such as login systems, duplicate detection, search engines, and large-scale data analysis.