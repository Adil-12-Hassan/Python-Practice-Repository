# A Program to Count Unique Values.

numbers = [10, 20, 30, 20, 40, 30, 50]

unique_values = set(numbers)

print("Unique Values:", unique_values)
print("Total Unique Values:", len(unique_values))

# Explanation:
# The program begins with a list containing duplicate values. The set() function removes all repeated elements, leaving only unique values. The len() function then counts how many unique elements remain and displays the result.

# Real-Life Use:
# Counting unique values is useful for determining the number of unique users, products, visitors, or transactions.